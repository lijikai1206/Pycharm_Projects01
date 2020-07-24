# 此例示范assert语句的用法
def get_age():
    a = int(input('请输入年龄：'))
    # 以下语句会在a不在【0,140】时触发AssertionError错误
    assert 0 <= a <= 140, '年龄不在合法的范围内'
    return a

try:
    age = get_age()
except AssertionError as e:
    print('错误的原因是：', e)
    age = 0
print('年龄是：', age)