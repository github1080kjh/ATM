# ATM
实现ATM和实现商城购物的某些功能


ATM-and-shopping
简单购物，付款

运行环境：python3.6.5（不兼容Python2.x）

实现功能

1.额度可以自定义
2.实现购物商城，买东西，可以加入购物车
3.支持多用户登录
4.可以添加新用户
5.可以修改用户密码
6.购物时记录日志
7.atm消费日志
8.实现转账

未实现功能：

1.可以提现，手续费5%
2.提供还款接口
3.使用装饰器实现用户认证

注意：整个程序的接口是bin/bin.py ，可以直接运行程序，可以直接上手运行，程序中有提示各种操作的方法

文件详情：
ATM——logger：
>>init.py
>>atm_logger.py ： 实现记录ATM类的日志记录功能
>>atm_logging_info ： 存放ATM类型的日志记录

bin:
>>init.py
>>bin.py # 整个程序的入口

login_info:
>>init.py
>>login.py ： 实现登录功能，可多用户登录
>>user_info ：存储用户的账号和密码
>>add_user.py： 实现添加用户的功能
>>login_info.py ：

moudle:
>>init.py
>>shopping.py ： 实现展示商品的功能和购买商品的功能

setting:
>>init.py
>>money ： 存放每个用户的可用余额
>>money_info.py ： 付钱的接口
>>transfer.py  : 转账的接口

shopping_logger:
>>init.py
>>logger.py ：实现记录普通的购物日志功能
>>logger_info ： 存储普通日志
