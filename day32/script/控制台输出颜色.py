# python控制台颜色打印
# https://blog.csdn.net/wangjian1204/article/details/82056496
# 格式：\033[显示方式;前景色;背景色m要打印的字符串\033[0m

# 前景色               背景色                 颜色
# 30	                40	                  黑色
# 31	                41	                  红色
# 32	                42	                  绿色
# 33	                43	                  黃色
# 34	                44	                  蓝色
# 35	                45	                 紫红色
# 36	                46	                 青蓝色
# 37	                47	                   白色

# 显示方式	                意义
#   0	                终端默认设置
#   1	                高亮显示
#   4	                使用下划线
#   5	                 闪烁
#   7	                反白显示
#   8	                不可见
#   22                非粗体
#   24                非下划线
#   25                非闪烁

ANSI_BLACK = 30
ANSI_RED = 31
ANSI_GREEN = 32
ANSI_YELLOW = 33
ANSI_BLUE = 34
ANSI_PURPLE = 35
ANSI_CYAN = 36
ANSI_WHITE = 37

ANSI_BLACK_BACKGROUND = 40
ANSI_RED_BACKGROUND = 41
ANSI_GREEN_BACKGROUND = 42
ANSI_YELLOW_BACKGROUND = 43
ANSI_BLUE_BACKGROUND = 44
ANSI_PURPLE_BACKGROUND = 45
ANSI_CYAN_BACKGROUND = 46
ANSI_WHITE_BACKGROUND = 47

MOD_DEFAULT = 0
MOD_HIGHLIGHT = 1
MOD_UNDERLINE = 4
MOD_FLICKER = 5
MOD_INVERSE = 7
MOD_HIDE = 8


def mod_print(message, fg=ANSI_WHITE, bg=ANSI_BLACK_BACKGROUND, mod=MOD_DEFAULT):
    """
    格式化输出
    :param message:
    :param fg:
    :param bg:
    :param mod:
    :return:
    """
    print('\033[{};{};{}m'.format(fg, bg, mod) + message + '\033[0m')


mod_print("python colorful print", ANSI_GREEN, ANSI_BLACK_BACKGROUND, MOD_UNDERLINE)
mod_print("python colorful print", ANSI_RED, ANSI_WHITE_BACKGROUND, MOD_UNDERLINE)
mod_print("python colorful print", ANSI_YELLOW, ANSI_BLACK_BACKGROUND, MOD_HIGHLIGHT)
mod_print("python colorful print", ANSI_YELLOW, ANSI_BLACK_BACKGROUND, MOD_UNDERLINE)

# https://www.cnblogs.com/Eva-J/p/8330517.html

# print('\033[0;36m爆竹声中一岁除，')
# print('春风送暖入屠苏。')
# print('千门万户曈曈日，')
# print('总把新桃换旧符。')
# print('hhhh\033[4m')
# print(1)
