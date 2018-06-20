#__author: kangkang
#date : 2018/6/18 0018


import configparser

# 为新用户添加余额，新用户也可以实现用户之间的转账
def add_user_money(username):
    config = configparser.ConfigParser()

    config.read(r'H:\project coding\setting\money')

    config[username] = {username: '15000'}  # 给新用户添加余额

    config.write(open(r'H:\project coding\setting\money', 'w'))  # 重新写入文件




# 添加用户的函数
def add_user(username, password):
    config = configparser.ConfigParser()

    config.read(r'H:\project coding\login_info\user_info')
    config[username] = {username: password}   # 用configparser写入新的用户和密码

    config.write(open(r'H:\project coding\login_info\user_info', 'w'))  # 将新用户的信息保存下来

    add_user_money(username)  # 调用函数，为新用户添加余额

    print('add user success!') # 提示添加成功


if __name__ == '__main__':
    add_user('mark', '123')
