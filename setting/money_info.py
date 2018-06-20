#__author: kangkang
#date : 2018/6/18 0018

import configparser

# atm日志
from ATM_logger import atm_logger

# 消费商品日志
from shopping_logger import logger

# 付钱的接口
def pay_money(username, thing, spend):
    config = configparser.ConfigParser()

    config.read(r'H:\project coding\setting\money')     # 拿到操作文件的权限

    before_money = config[username][username]
    config.set(username, username, str(int(before_money)-int(spend)))  # 将花费的钱减去

    config.write(open(r'H:\project coding\setting\money', 'w'))  # 写入修改后的文件


    # atm日志内容格式
    atm_message = ''.join([username, ' spend ', str(spend), ' $, now you have', str(int(before_money)-int(spend)), ' $'])
    # print(atm_message)
    atm_logger.write_atm_logger(atm_message)   # 将花费情况写入atm日志并且打印在屏幕上

    # 普通消费日志的内容格式
    shopping_message = ' '.join([username, 'spend', str(spend), '$, for', thing])
    # print(shopping_message)
    logger.write_logger(shopping_message)   # 购买的东西，和花费写入普通日志

    print('pay success!')

if __name__ == '__main__':

    pay_money('kangjunhao', 'bed', '5000')