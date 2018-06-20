#__author: kangkang
#date : 2018/6/19 0019

from ATM_logger import atm_logger  # 调用记录日志的模块

import configparser

# 转账实现, 三个参数，付款方，收款方，转账金额
def transfer(pay_people, accept_people, money):
    config = configparser.ConfigParser()

    config.read(r'H:\project coding\setting\money')

    # 转账方，减去转账金额
    config.set(pay_people, pay_people, str(int(config[pay_people][pay_people])-int(money)))
    # 收款方，加上转账金额
    config.set(accept_people, accept_people, str(int(config[accept_people][accept_people])+int(money)))


    config.write(open(r'H:\project coding\setting\money', 'w'))  # 将修改以后的金额存进文件

    logger_format = ' '.join([pay_people, 'transfer to', accept_people, money, '$'])

    atm_logger.write_atm_logger(logger_format)

    print('accept success!')   # 提示转账成功
if __name__ == '__main__':
    transfer('kangjunhao', 'alex', '5000')