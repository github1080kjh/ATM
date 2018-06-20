#__author: kangkang
#date : 2018/6/18 0018

import os
import sys

# ret = os.path.dirname(os.getcwd())
exit_flag = True  # 控制退出的标志位

while exit_flag == True:

    sys.path.append(os.path.dirname(os.getcwd()))  # 将项目的根路径添加到搜索路径中

    from moudle import shopping


    shopping.shopping_show()      # 展示商品

    your_choice = input('Do you want to buy ?')  # 用户输入想要购买的商品
    your_name = input('who are you?')         # 用于添加购物车，因为在添加购物车之前不需要登录


    shopping.choice_shopping(your_name, your_choice)      # 调用这个函数支付，选择，添加购物车，等等

    is_exit = input('exit this project ?(yes/no)')
    if is_exit == 'yes':
        print('welcome again!')
        exit_flag = False    # 重新赋值标志位，控制退出程序





