
#1.添加一个余额变动提醒的短消息提醒功能
def messend_send(fn):
    def fx(name, x):
        print("发送消息：", name, "来银行办理业务....")
        fn(name,x)
        print("发送消息：",name, "办理了",x,"元的业务....")
    return fx
#2.加一个权限验证功能
def pricileged_check(fn):
    def fx(name, x):
        print("正在检测权限....")
        if True:
            fn(name, x)
    return fx

@pricileged_check
@messend_send
def savemoney(name,x):
    print(name,"存钱",x,"元")
@messend_send
def withdraw(name,x):
    print(name,'取钱',x,'元')

#程序调用
savemoney('小李',200)
#savemoney('小赵',500)
#withdraw('小王',300)