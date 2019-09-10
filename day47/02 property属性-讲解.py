# property属性

# 1. 什么是property属性


class Goods:

    @property
    def size(self):
        return 100


obj = Goods()
ret = obj.size
# print(ret)
# 输出
# 100

# property属性的定义和调用要注意一下几点
# 定义时，在实例方法的基础上添加@property装饰器；并且仅有一个self参数
# 调用时，无需括号

# 2. 简单的实例


class Pager:
    def __init__(self, current_page):
        self.current_page = current_page
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = self.current_page * self.per_items
        return val


p = Pager(1)
# print(p.start)
# print(p.end)
# 输出
# 0
# 10


# Python的property属性的功能是：property属性内部进行一系列的逻辑计算，最终将计算结果返回


# 3. property属性的有两种方式

# 装饰器 在方法上应用装饰器
# 类属性 在类中定义值为property对象的类属性

# 3.1 装饰器方式

# 经典类中的属性只有一种访问方式，其对应被 @property 修饰的方法
# 新式类中的属性有三种访问方式，并分别对应了三个被@property、@方法名.setter、@方法名.deleter修饰的方法

# 由于新式类中具有三种访问方式，我们可以根据它们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除


class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


obj = Goods()

# 获取商品价格
# 自动执行@property修饰的price方法，并获取方法的返回值
price = obj.price
# print(price)

# 修改商品原价
# 自动执行@price.setter修饰的 price 方法，并将200赋值给方法的参数
obj.price = 200
# print(obj.price)

# 删除商品原价
# 自动执行 @price.deleter 修饰的price方法
# del obj.price

# 3.2 类属性方式，创建值为property对象的类属性


# 当使用类属性的方式创建property属性时，经典类和新式类无区别

# property方法中有个四个参数
# 第一个参数是方法名，调用 对象.属性 时自动触发执行方法
# 第二个参数是方法名，调用 对象.属性 ＝ XXX 时自动触发执行方法
# 第三个参数是方法名，调用 del 对象.属性 时自动触发执行方法
# 第四个参数是字符串，调用 对象.属性.__doc__ ，此参数是该属性的描述信息


class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    BAR = property(get_bar, set_bar, del_bar, "description...")


obj = Foo()

# 自动调用第一个参数中定义的方法：get_bar
# obj.BAR

# 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
# obj.BAR = "alex"

# 自动获取第四个参数中设置的值：description...
desc = Foo.BAR.__doc__
# print(desc)

# 自动调用第三个参数中定义的方法：del_bar方法
# del obj.BAR

# 由于类属性方式创建property属性具有3种访问方式
# 我们可以根据它们几个属性的访问特点，分别将三个方法定义为对同一个属性：获取、修改、删除


class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述...')


obj = Goods()

# 获取商品价格
# print(obj.PRICE)

# 修改商品原价
obj.PRICE = 200

# 删除商品原价
del obj.PRICE

# 定义property属性共有两种方式，分别是 装饰器和 类属性，而装饰器方式针对经典类和新式类又有所不同
# 通过使用property属性，能够简化调用者在获取数据的流程

