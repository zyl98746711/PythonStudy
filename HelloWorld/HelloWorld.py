from pip._vendor.distlib.compat import raw_input

print('Hello World')

name = raw_input("按下 enter 键退出，其他任意键显示...\n"
                 "请输入：")

print(name)
