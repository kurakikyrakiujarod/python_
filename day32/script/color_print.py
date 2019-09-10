# import random
#
#
# def color_print(msg):
#     fg = random.randint(30, 37)
#     # bg = random.randint(40, 47)
#     # mod = random.randint(0, 8)
#     # return '\033[{};{};{}m'.format(fg, bg, mod) + msg + '\033[0m'
#     # return '\033[{};{}m'.format(fg, mod) + msg + '\033[0m'
#     return '\033[{}m'.format(fg) + msg + '\033[0m'
#
#
# print(color_print('python colorful print'))

# from collections import OrderedDict
#
#
# def customize():
#     choices = []
#     # 前景色
#     fg = OrderedDict(ANSI_BLACK=30, ANSI_RED=31, ANSI_GREEN=32, ANSI_YELLOW=33,
#                      ANSI_BLUE=34, ANSI_PURPLE=35, ANSI_CYAN=36, ANSI_WHITE=37)
#     # 背景色
#     bg = OrderedDict(ANSI_BLACK_BACKGROUND=40, ANSI_RED_BACKGROUND=41, ANSI_GREEN_BACKGROUND=42,
#                      ANSI_YELLOW_BACKGROUND=43, ANSI_BLUE_BACKGROUND=44, ANSI_PURPLE_BACKGROUND=45,
#                      ANSI_CYAN_BACKGROUND=46, ANSI_WHITE_BACKGROUND=47)
#     # 显示模式
#     mod = OrderedDict(MOD_DEFAULT=0, MOD_HIGHLIGHT=1, MOD_UNDERLINE=4, MOD_FLICKER=5, MOD_INVERSE=7, MOD_HIDE=8)
#     fg.update(bg)
#     fg.update(mod)
#
#     for index, item in enumerate(fg, 1):
#         if index < 8:
#             print(index, item + '(前景色)', end=' ')
#         elif index == 8:
#             print(index, item + '(前景色)')
#         elif 8 < index < 15:
#             print(index, item + '(背景色)', end=' ')
#         elif index == 16:
#             print(index, item + '(背景色)')
#         else:
#             print(index, item + '(显示方式)', end='')
#
#     fg_choice = int(input('\n请选择前景色(1-8):'))
#     bg_choice = int(input('请选择背景色(9-16):'))
#     mod_choice = int(input('请选择显示方式(17-22):'))
#     choices.append(fg[list(fg)[fg_choice - 1]])
#     choices.append(fg[list(fg)[bg_choice - 1]])
#     choices.append(fg[list(fg)[mod_choice - 1]])
#     return tuple(choices)
#
#
# if __name__ == '__main__':
#     print(customize())

