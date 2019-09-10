import re

import uiautomator2 as u2

import handle_mongo

__all__ = ['ParentChartArticleSpider']


class ParentChartArticleSpider(object):
    def __init__(self, serial, tab_text):
        self.serial = serial
        self.d = u2.connect(self.serial)
        self.tab_text = tab_text
        self.mogo = handle_mongo.ConnectMongo()

    def swipe_down(self, num):
        width, height = self.d.window_size()
        x1 = width / 2
        y1 = 720
        y = 900
        for i in range(num):
            self.d.swipe(x1, y, x1, y1)

    def is_photo(self, content):
        zhmodel = re.compile(u'[\u4e00-\u9fa5]')
        match = zhmodel.search(content)
        if content.endswith('.png') or content.endswith('.jpg'):
            return True
        if not match and content.isalnum() and len(content) > 10:
            return True
        return False

    def get_article(self):
        content_list = list()
        article = dict()
        repeat_count = 0
        FLAG = True
        while FLAG:
            if self.d(text='最新评论').exists(timeout=3) or \
                    self.d(resourceId='cn.com.askparents.parentchart:id/text_lookmore', text='查看更多评论').exists(
                        timeout=3) or self.d(text='延伸阅读').exists(timeout=3):
                FLAG = False

            if self.d(resourceId='cn.com.askparents.parentchart:id/text_likenumber').exists(timeout=3):
                like_num = self.d(resourceId='cn.com.askparents.parentchart:id/text_likenumber').get_text()
                article['like_num'] = int(like_num.replace('+', ''))
            else:
                article['like_num'] = 0

            for elem in self.d.xpath("//android.view.View").all():
                if '版权声明：本文仅代表作者观点，不代表家长口袋立场。' in elem.attrib['content-desc']:
                    FLAG = False
                    continue
                if elem.attrib['clickable'] == 'true':
                    if elem.attrib['content-desc'] not in content_list:
                        content_list.append(elem.attrib['content-desc'])
                        print(elem.attrib['content-desc'])
                        if self.is_photo(elem.attrib['content-desc']):
                            title = content_list[0].strip().replace(' ', '').replace('、', '').replace('|', '')
                            photo_name = title + '_' + elem.attrib['content-desc'] + '.jpg'
                            print('保存图片\n{}'.format(photo_name))
                            self.d.xpath(
                                '//*[@content-desc="%s"]' % elem.attrib['content-desc']).get().screenshot().save(
                                'imgs/{}'.format(photo_name))
                        repeat_count = 0
                    else:
                        repeat_count += 1
                        print('Repeat{}'.format(repeat_count))
                        if repeat_count > 30:
                            FLAG = False
            self.swipe_down(5)

            # else:
            #     print('真机')
            #     for elem in self.d.xpath("//android.view.View").all():
            #         if elem.attrib['text'] not in content_list \
            #                 and not elem.attrib['text'].isspace() \
            #                 and elem.attrib['text']:
            #             content_list.append(elem.attrib['text'])
            #             print(elem.attrib['text'])
            #             repeat_count = 0
            #             if self.is_photo(elem.attrib['text']):
            #                 print('保存图片\n{}'.format(content_list[0] + '_' + elem.attrib['text'] + '.jpg'))
            #                 self.d.xpath(
            #                     '//*[@text="%s"]' % elem.attrib['text']).get().screenshot().save(
            #                     'imgs/{}'.format(content_list[0] + '_' + elem.attrib['text'] + '.jpg'))
            #         else:
            #             print(elem.attrib['text'])
            #             repeat_count += 1
            #             print('Repeat{}'.format(repeat_count))
            #             if repeat_count > 30:
            #                 FLAG = False
            #
            #     self.swipe_down(5)

        if content_list:
            article['title'] = content_list.pop(0)
            article['author'] = content_list.pop(0)
            article['review_num'] = content_list.pop(0)
            article['content'] = '\n'.join(content_list)
        return article

    # def get_imgs(self):
    #     num_text = self.d(resourceId='cn.com.askparents.parentchart:id/text_title').get_text()
    #     num = int(num_text.replace('人参与评论', ''))
    #     for i in range(1, num + 1):
    #         try:
    #             name1 = self.d.xpath(
    #                 '//*[@resource-id="cn.com.askparents.parentchart:id/list"]/android.widget.RelativeLayout[%d]//android.widget.TextView' % i).get_text()
    #             self.d.xpath(
    #                 '//*[@resource-id="cn.com.askparents.parentchart:id/list"]/android.widget.RelativeLayout[%d]//android.widget.ImageView' % i).get().screenshot().save(
    #                 'imgs/{}'.format(name1 + '.jpg'))
    #         except XPathElementNotFoundError as e:
    #             print(e)
    #             return

    def get_review(self):
        repeat_count = 0
        FLAG = True
        info_dict = dict()
        content_list = list()
        base_id = 'cn.com.askparents.parentchart:id/'
        attrs = ['text_name1', 'text_time', 'text_fromname', 'text_toname', 'text_content']

        if self.d(resourceId='cn.com.askparents.parentchart:id/text_reviewnum').exists(timeout=3):
            self.d(resourceId='cn.com.askparents.parentchart:id/text_reviewnum').click()
            while FLAG:
                elems = self.d.xpath('//android.widget.TextView').all()
                for elem in elems:
                    for attr in attrs:
                        if elem.attrib['resource-id'] == (base_id + attr):
                            format_content = elem.attrib['resource-id'].split('_')[-1] + ':' + elem.attrib['text']
                            if format_content not in content_list:
                                print(format_content)
                                content_list.append(format_content)
                            else:
                                repeat_count += 1
                                print('Repeat{}'.format(repeat_count))
                                self.swipe_down(2)
                                if repeat_count > 30:
                                    FLAG = False
            info_dict['reply_page'] = '\n'.join(content_list)
            if self.d(resourceId='cn.com.askparents.parentchart:id/img_back').exists(timeout=3):
                self.d(resourceId='cn.com.askparents.parentchart:id/img_back').click()
        return info_dict

    def get_one_paper(self):
        article = self.get_article()
        review = self.get_review()
        article.update(review)
        self.mogo.add_one(self.tab_text, article)
        print(article)
        if self.d(resourceId='cn.com.askparents.parentchart:id/img_back').exists(timeout=3):
            self.d(resourceId='cn.com.askparents.parentchart:id/img_back').click()

    def get_one_photo(self, title, photo_text):
        for elem in self.d.xpath("//android.view.View").all():
            if elem.attrib['content-desc'] == photo_text:
                title = title.strip().replace(' ', '').replace('、', '').replace('|', '')
                photo_name = title + '_' + elem.attrib['content-desc'] + '.jpg'
                print('save photo ', photo_name)
                self.d.xpath(
                    '//*[@content-desc="%s"]' % photo_text).get().screenshot().save(
                    'imgs/{}'.format(photo_name))
                break

    def run(self):
        while True:
            if self.d(resourceId='cn.com.askparents.parentchart:id/tv_article_title').exists(timeout=3):
                article_title = self.d(resourceId='cn.com.askparents.parentchart:id/tv_article_title').get_text()
                print('article title is \n{}'.format(article_title))
                self.d(resourceId='cn.com.askparents.parentchart:id/tv_article_title').click()
                self.get_one_paper()
                self.swipe_down(1)


if __name__ == '__main__':
    spider = ParentChartArticleSpider('127.0.0.1:62001', '上海幼升小_0830')
    # spider.run_topic_papers()
    spider.get_one_paper()
    # spider.run_topic_papers()
    # spider.get_imgs()
    # spider.get_article()
    # spider.get_one_photo('探校|常青藤幼儿园——一所让孩子不想回家的幼儿园', 'blob.png')
