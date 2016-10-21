class toycar:
    def __init__(self, shape, price):
        self.shape = shape
        self.price = price

    def getshape(self):
        return self.shape

    def getprice(self):
        return self.price

class bread:
    def __init__(self, status, price):
        self.status = status
        self.price = price

    def getstatus(self):
        return self.status

    def getprice(self):
        return self.price

class storekeeper:
    def __init__(self, name, order):
        self.name = name
        self.toy = toycar('cycle', '20')
        self.food = bread('not expired', '10')
        self.answer(order)

    def checktoycar(self):
        print('%s: The shape of the toy car is %s.' % (self.name, self.toy.shape))
        print('%s: The price of the toy car is %s yuan.' % (self.name, self.toy.price))

    def checkbread(self):
        print('%s: The status of the bread is %s.' % (self.name, self.food.status))
        print('%s: The price of the bread is %s yuan.' % (self.name, self.food.price))

    def answer(self, order):
        if order == 'toys':
            print('%s: We have a toy car if you like.' % self.name)
            self.checktoycar()
        elif order == 'food':
            print('%s :We have some bread if you like.' % self.name)
            self.checkbread()
        else:
            print('%s: Sorry, no such thing here.' % self.name)


class customer:
    def __init__(self, name, item):
        self.name = name
        self.item = item

    def ask(self):
        print('%s: I want some  %s' % (self.name, self.item))
        return self.item

if __name__ == '__main__':
    person1 = customer('Bob', 'food')
    person2 = storekeeper('Peter', person1.ask())

