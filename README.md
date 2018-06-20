# ATM
实现ATM和实现商城购物的某些功能<br><br><br>


ATM-and-shopping<br>
简单购物，付款<br><br>

运行环境：python3.6.5（不兼容Python2.x）<br><br>

实现功能<br><br>

1.额度可以自定义<br>
2.实现购物商城，买东西，可以加入购物车<br>
3.支持多用户登录<br>
4.可以添加新用户<br>
5.可以修改用户密码<br>
6.购物时记录日志<br>
7.atm消费日志<br>
8.实现转账<br><br>

未实现功能：<br><br>

1.可以提现，手续费5%<br>
2.提供还款接口<br>
3.使用装饰器实现用户认证<br><br>

注意：整个程序的接口是bin/bin.py ，可以直接运行程序，可以直接上手运行，程序中有提示各种操作的方法<br><br>

文件详情：<br>
ATM——logger：<br>
>>init.py<br>
>>atm_logger.py ： 实现记录ATM类的日志记录功能<br>
>>atm_logging_info ： 存放ATM类型的日志记录<br><br>

bin:<br>
>>init.py<br>
>>bin.py # 整个程序的入口<br><br>

login_info:<br>
>>init.py<br>
>>login.py ： 实现登录功能，可多用户登录<br>
>>user_info ：存储用户的账号和密码<br>
>>add_user.py： 实现添加用户的功能<br>
>>login_info.py ：<br><br>

moudle:<br>
>>init.py<br>
>>shopping.py ： 实现展示商品的功能和购买商品的功能<br><br>

setting:<br>
>>init.py<br>
>>money ： 存放每个用户的可用余额<br>
>>money_info.py ： 付钱的接口<br>
>>transfer.py  : 转账的接口<br><br>

shopping_logger:<br>
>>init.py<br>
>>logger.py ：实现记录普通的购物日志功能<br>
>>logger_info ： 存储普通日志<br>
