import re

bracket = re.compile(r'\([^()]+\)')  # 寻找最内层括号规则
mul = re.compile(r'(\d+\.?\d*\*-\d+\.?\d*)|(\d+\.?\d*\*\d+\.?\d*)')  # 寻找乘法运算规则
div = re.compile(r'(\d+\.?\d*/-\d+\.?\d*)|(\d+\.?\d*/\d+\.?\d*)')  # 寻找除法运算规则
add = re.compile(r'(-?\d+\.?\d*\+-\d+\.?\d*)|(-?\d+\.?\d*\+\d+\.?\d*)')  # 寻找加法运算规则
sub = re.compile(r'(-?\d+\.?\d*--\d+\.?\d*)|(-?\d+\.?\d*-\d+\.?\d*)')  # 寻找减法运算规则
c_f = re.compile(r'\([^*/]\)')  # 检查括号内是否运算完毕规则
strip = re.compile(r'[^(].*[^)]')  # 脱括号规则
n_md = re.compile('\([^*/]+\)')  # 一个括号里面没有乘除 那么只会有数字与加减
res = re.compile('([+-]?\d+\.?\d*)')
ills = re.compile(r'[^0-9*/+\-\(\)]')  # 判断用户输入是否非法


# 计算乘法
def Mul(exp):
    # 分割
    result = re.split(r'\*', mul.search(exp).group())
    # 执行计算，并替换表达式，最终转换为字符串方便进一步操作
    return exp.replace(mul.search(exp).group(), str(float(result[0]) * float(result[1])))


# 计算除法
def Div(exp):
    result = re.split(r'/', div.search(exp).group())
    return exp.replace(div.search(exp).group(), str(float(result[0]) / float(result[1])))


# 计算加法减法
def Add_Sub(exp):
    # 将多余的符号替换掉
    exp = exp.replace('++', '+')
    exp = exp.replace('+-', '-')
    exp = exp.replace('--', '+')
    exp = exp.replace('-+', '-')
    # 返回的列表包含了所以的数字
    nums = re.findall('[+\-]?\d+\.?\d*', exp)
    count = 0
    # 遍历相加
    for num in nums:
        count += float(num)
    return str(count)


# 没有添加用户输入判断
def calculator():
    while True:
        exp = input('>>>')
        round_num = input('请输入保留位数,输入为空不保留：')
        # 判断用户退出 退出循环
        if exp.strip().upper() == 'Q':
            print('退出程序')
            # exit()
            break
        # 不退出 进入执行逻辑
        else:
            # 得到小数点保留位数
            try:
                # 如果用户输入为空  round_num = None
                # 将字符串转换为数字
                round_num = None if round_num.strip() == '' else int(round_num)
            # 捕获字符串转换过程出现的异常并round_num = None
            except Exception as e:
                print(e)
                print('输入非法，不保留小数位')
                round_num = None
            # 删除所有的空格
            exp = exp.replace(' ', '')
            # 判断用户输入是否非法
            if ills.search(exp):
                print('有非法字符!')
            else:
                # 用户输入合法
                while bracket.search(exp):
                    # 寻找最内层括号
                    result = bracket.search(exp).group()
                    # 计算除法
                    if div.search(result):
                        exp = exp.replace(result, Div(result))
                    # 计算乘法
                    elif mul.search(result):
                        exp = exp.replace(result, Mul(result))
                    # 将括号里面的内容做加减运算，得到的结果然后替换整个括号
                    elif n_md.search(result):
                        # exp = exp.replace(n_md.search(result).group(),Add_Sub(result))
                        exp = exp.replace(result, Add_Sub(result))
                        print(exp)
                # 没有括号了，操作整个表达式，先算乘除，再算加减
                while True:
                    if div.search(exp):
                        result = div.search(exp).group()
                        exp = exp.replace(result, Div(result))
                    elif mul.search(exp):
                        result = mul.search(exp).group()
                        exp = exp.replace(result, Mul(result))
                    else:
                        result = Add_Sub(exp)
                        # print('The answer is: %.2f'%float(result))

                        print('The answer is: {}'.format(round(float(result), round_num)))
                        break


calculator()
# print(1-2*((60-30+(-40/-5+20/4+3*4*5/2)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))-99*2)
# print(69*(69+1)*100+2*8)
