#__author: kangkang
#date : 2018/6/18 0018

# 登录函数
import configparser  # 配置日志文件

from login_info import change_passwd # 调用修改密码的接口

from login_info import add_user   # 调用添加新用户的接口

def login(username, password):
    login_result = False  # 先定义未登录
    config = configparser.ConfigParser()

    config.read(r'H:\project coding\login_info\user_info')  # 读取文件

    if username in config.sections() and password == config[username][username]: # 判断账户和密码是否正确
        print('login success!')
        login_result = True  # 如果登录成功就将login_result重新赋值

        # 询问用户是否需要修改账户密码，只有在你登录成功以后才能修改你的密码
        is_change_password = input('can you need change your password?(yes/no)')
        if is_change_password == 'yes':
            your_new_password = input('please input your new password:')  # 提示输入用户的新密码
            change_passwd.change_passwd(username, your_new_password) # 调用修改密码的函数

        # 询问用户是否需要添加新的用户
        is_add_user = input('can you need add a new user?(yes/no)')
        if is_add_user == 'yes':
            new_user_name = input('new name:')
            new_password = input('your password:')
            add_user.add_user(new_user_name, new_password)  # 调用接口添加新用户

    else:
        print('login fail!')

    return login_result


    # print(config.sections())
    # print(config['kangjunhao']['kangjunhao'])

# with open(r'H:\project coding\first test\login_info\user_info', 'r') as file:
#     info = dict(file.read())
#     for i in info:
#         print(i)

if __name__ == '__main__':
    login('alex', '123')