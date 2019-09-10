import re
import datetime

import uiautomator2 as u2

import handle_mongo


class ParentChartSpider(object):
    def __init__(self, serial, tab_text):
        self.d = u2.connect(serial)
        self.tab_text = tab_text
        self.mogo = handle_mongo.ConnectMongo()

    # 向下滑动
    def swipe_down(self, num):
        width, height = self.d.window_size()
        x1 = width / 2
        y1 = 720
        y = 900
        for i in range(num):
            self.d.swipe(x1, y, x1, y1)

    def parse_time(self, time_content):
        if not re.findall('201[7,8,9]', time_content):
            time_content = str(datetime.datetime.now().year) + '-' + time_content
        return time_content

    def get_question(self):
        result = {}
        if self.d(resourceId='cn.com.askparents.parentchart:id/text_content').exists(timeout=3):
            question_content = self.d(resourceId='cn.com.askparents.parentchart:id/text_content').get_text()
            question_content = question_content.replace('\r', '').replace('\n', '').strip()
            if len(question_content.split('#')) == 2:
                question = question_content.split('#')[0]
                school = question_content.split('#')[1]
            else:
                question = question_content
                school = '没有学校信息'
            result['question'] = question
            result['school'] = school
            if self.d(resourceId='cn.com.askparents.parentchart:id/text_time').exists():
                result['question_time'] = self.parse_time(
                    self.d(resourceId='cn.com.askparents.parentchart:id/text_time').get_text())
            if self.d(resourceId='cn.com.askparents.parentchart:id/text_name').exists():
                result['name'] = self.d(resourceId='cn.com.askparents.parentchart:id/text_name').get_text()
            if self.d(resourceId='cn.com.askparents.parentchart:id/text_zhuiwen').exists():
                result['question_deatil'] = self.d(
                    resourceId='cn.com.askparents.parentchart:id/text_zhuiwen').get_text()
            if self.d(resourceId='cn.com.askparents.parentchart:id/text_zhuiwentime').exists():
                question_deatil_time = self.d(
                    resourceId='cn.com.askparents.parentchart:id/text_zhuiwentime').get_text()
                result['question_deatil_time'] = self.parse_time(question_deatil_time)
        return result

    def get_answers(self):
        answer_list = []
        nums = 3
        self.swipe_down(2)
        if self.d(resourceId='cn.com.askparents.parentchart:id/text_answennum').exists(timeout=5):
            nums = int(self.d(resourceId='cn.com.askparents.parentchart:id/text_answennum').get_text().replace(
                '个回答', ''))
        if self.d(resourceId='cn.com.askparents.parentchart:id/anslist').exists(timeout=5):
            try:
                for num in range(nums):
                    answer = {}
                    time_content = self.d(resourceId="cn.com.askparents.parentchart:id/anslist").child_by_instance(
                        resourceId="cn.com.askparents.parentchart:id/text_time", inst=num).get_text()
                    answer_content = self.d(
                        resourceId="cn.com.askparents.parentchart:id/anslist").child_by_instance(
                        resourceId="cn.com.askparents.parentchart:id/text_content", inst=num).get_text()
                    answer_name = self.d(resourceId="cn.com.askparents.parentchart:id/anslist").child_by_instance(
                        resourceId="cn.com.askparents.parentchart:id/text_name", inst=num).get_text()
                    answer['answer_time'] = self.parse_time(time_content)
                    answer['answer_name'] = answer_name
                    answer['answer_content'] = answer_content

                    # if self.d(resourceId='cn.com.askparents.parentchart:id/ll_answelist').exists(timeout=3):
                    #     if self.d(resourceId='cn.com.askparents.parentchart:id/text_fromname').exists(timeout=3):
                    #         reply_name = self.d.xpath(
                    #             '//*[@resource-id="cn.com.askparents.parentchart:id/text_fromname"]').get_text()
                    #         reply_content = self.d.xpath(
                    #             '//*[@resource-id="cn.com.askparents.parentchart:id/ll_content"]/android.widget.TextView[1]').get_text()
                    #         reply_time = self.d.xpath(
                    #             '//*[@resource-id="cn.com.askparents.parentchart:id/ll_content"]/android.widget.TextView[2]').get_text()
                    #         answer['reply_name'] = reply_name
                    #         answer['reply_content'] = reply_content
                    #         answer['reply_time'] = self.parse_time(reply_time)
                    # print('{}次{}'.format(num, answer))
                    answer_list.append(answer)
            except Exception as e:
                print(e)
                # self.swipe_down(1)
            finally:
                return answer_list
        else:
            return answer_list

    def merge_question_answers(self, question, answers):
        question['answers_num'] = len(answers)
        for index, answer in enumerate(answers, 1):
            tmp_dict = dict()
            tmp_dict['answer' + str(index)] = '{},{}:{}'.format(answer['answer_name'],
                                                                answer['answer_time'],
                                                                answer['answer_content'])
            question.update(tmp_dict)

    def run(self):
        signature_set = set()
        repeat_count = 0
        while True:
            if self.d(text=self.tab_text).exists(timeout=5):
                self.d(text=self.tab_text).click()
            if self.d(resourceId='cn.com.askparents.parentchart:id/text_question').exists(timeout=5):
                self.d(resourceId="cn.com.askparents.parentchart:id/text_question").click()
                question = self.get_question()
                if question:
                    answers = self.get_answers()
                    self.merge_question_answers(question, answers)
                    signature = str(question)
                    if signature in signature_set:
                        repeat_count += 1
                    else:
                        repeat_count = 0
                        signature_set.add(signature)
                        self.mogo.add_one(self.tab_text, question)
                        print('已经爬取了{}条数据'.format(len(signature_set)))
                        print(question)

            if self.d(resourceId='cn.com.askparents.parentchart:id/img_back').exists(timeout=5):
                self.d(resourceId="cn.com.askparents.parentchart:id/img_back").click()

            if repeat_count >= 10:
                print('到达底部')
                # break
            self.swipe_down(2)

    def get_one_page(self):
        question = self.get_question()
        self.merge_question_answers(question, self.get_answers())
        self.mogo.add_one(self.tab_text, question)
        print(question)

    def get_one_answer(self, num=0):
        result = {}
        if self.d(resourceId='cn.com.askparents.parentchart:id/text_content').exists(timeout=5):
            time_content = self.d(resourceId="cn.com.askparents.parentchart:id/anslist").child_by_instance(
                resourceId="cn.com.askparents.parentchart:id/text_time", inst=num).get_text()
            answer_content = self.d(
                resourceId="cn.com.askparents.parentchart:id/anslist").child_by_instance(
                resourceId="cn.com.askparents.parentchart:id/text_content", inst=num).get_text()
            answer_name = self.d(resourceId="cn.com.askparents.parentchart:id/anslist").child_by_instance(
                resourceId="cn.com.askparents.parentchart:id/text_name", inst=num).get_text()
            result['time_content'] = self.parse_time(time_content)
            result['answer_content'] = answer_content
            result['answer_name'] = answer_name
            # if self.d(resourceId='cn.com.askparents.parentchart:id/ll_answelist').exists(timeout=3):
            #     reply_name = self.d.xpath(
            #         '//*[@resource-id="cn.com.askparents.parentchart:id/text_fromname"]').get_text()
            #     reply_content = self.d.xpath(
            #         '//*[@resource-id="cn.com.askparents.parentchart:id/ll_content"]/android.widget.TextView[1]').get_text()
            #     reply_time = self.d.xpath(
            #         '//*[@resource-id="cn.com.askparents.parentchart:id/ll_content"]/android.widget.TextView[2]').get_text()
            #     result['reply_name'] = reply_name
            #     result['reply_content'] = reply_content
            #     result['reply_time'] = self.parse_time(reply_time)
            print(result)


if __name__ == '__main__':
    spider = ParentChartSpider('127.0.0.1:62001', '在校生活')
    # spider.get_one_page()
    # spider.get_one_answer(1)
    spider.run()