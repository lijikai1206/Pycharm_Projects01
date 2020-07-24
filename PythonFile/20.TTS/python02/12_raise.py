# 此例用于示意raise语句来发出异常通知
# 供try - except 语句来捕获

def make_except():
    print('开始。。。')
    #raise ZeroDivisionError    #手动触发一个错误通知
    e = ZeroDivisionError('被零除啦！！！')
    raise e    # 触发e绑定的错误，进入异常状态
    print('结束')

try:
    make_except()
    print("make_except 调用完毕！")
except ZeroDivisionError as err:
    print('出现了被零除的错误，已处理并转为正常状态！')
    print('err绑定的对象是：', err)