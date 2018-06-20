#__author: kangkang
#date : 2018/6/18 0018

from login_info import login   # 调用登录接口

from setting import money_info  # 调用支付接口

from setting import transfer   # 调用转账接口

shopping_dict = {'apple': '10',               # 商品最原始的列表
                'banana': '20',
                'phone': '2000',
                'car': '200000',
                'bed': '5000'}
shopping_car = []    # 商品购物车

def shopping_show():         # 实现展示商品的效果
    print('shopping show'.center(60, '*'))
    for key, vaule in shopping_dict.items():
        print('%s ----> %s ' % (key, vaule))
    print('Ending'.center(60, '*'))


def choice_shopping(username, shopping):  # 选择商品的函数，参数是用户选择的商品
    if shopping in shopping_dict:

        is_add_shopping_car = input('add yourself shopping car?(yes/no)')
        if is_add_shopping_car == 'yes':
            shopping_car.append(shopping)  # 将商品放入购物车
            for thing in shopping_car:
                print('your shopping have a %s' % thing )


        is_buy = input('is pay now?(yes/no) ')
        if is_buy == 'yes':      # 如果用户需要支付，则调用登录接口
            id = input('your id :')
            password = input('your password :')
            if login.login(id, password) == True:          # 调用登陆接口


                money_info.pay_money(username, shopping, int(shopping_dict[shopping]))  # 调用付款接口支付

        is_transfer = input('is transfer now?(yes/no)')  # 提示用户是否需要转账
        if is_transfer == 'yes':
            pay_people = input('your name?')
            accept_people = input('accept name?')
            transfer_money = input('how money transfer to?')
            transfer.transfer(pay_people, accept_people, transfer_money)  # 执行转账函数




if __name__ == '__main__':
    shopping_show()
    choice_shopping('kangjunhao', 'apple')