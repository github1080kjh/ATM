# author: kangkang
# date : 2018/6/18 0018

import logging


# 记录日志模块
def write_logger(message):
    logger = logging.getLogger()      # 拿到logger

    file_handle = logging.FileHandler(r'H:\project coding\login_info\user_info')  # 设置文件和屏幕打印
    screen_handle = logging.StreamHandler()

    # 打印格式
    output_format = logging.Formatter('%(asctime)s -- %(levelname)s -- %(message)s')

    # 给输出方式添加输出格式
    file_handle.setFormatter(output_format)
    screen_handle.setFormatter(output_format)

    # 给logger添加输出方式
    logger.addHandler(file_handle)
    logger.addHandler(screen_handle)

    # 调整输出日志输出级别
    logger.setLevel(logging.DEBUG)

    logger.debug(message)