class A:
    def hello(self):
        print('A类的hello')


class B(A):
    def hello(self):
        print('B类的hello')

b = B()
super(B,b).hello()
