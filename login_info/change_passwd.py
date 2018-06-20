#__author: kangkang
#date : 2018/6/18 0018


import configparser

# config = configparser.ConfigParser()

# config['kangjunhao'] = {'kangjunhao': '123456'}
#
# config['alex'] = {'alex': '123'}
#
# config['alvin'] = {'alvin': '456'}
#
#
# config.write(open('user_info', 'w'))



# 修改密码的函数，参数是用户名和新密码
def change_passwd(username, new_passwd):
    config = configparser.ConfigParser()

    config.read(r'H:\project coding\first test\login_info\user_info')     # 拿到操作文件的权限

    config.set(username, username, new_passwd)  # 修改密码

    config.write(open(r'H:\project coding\first test\login_info\user_info', 'w'))  # 写入修改后的文件

    print('change password success!')

if __name__ == '__main__':

    change_passwd('kangjunhao', '1234')
