'''
  Using computer producing process to help understand the factory method pattern.
'''


class factory:
    def build(self):
        # real injection process
        print('Done.')


class computerA(factory):
    # build duck mold
    def __init__(self, name):
        self.name = name
        self.color = 'Black'
        print('You choose the computer A.')

    def buy(self):
        print('You are going to buy the computer A.')
        return self.build()


class computerB(factory):
    # build car mold
    def __init__(self, name):
        self.name = name
        self.size = 'Small'
        print('You choose the computer B.')

    def buy(self):
        print('You are going to buy the computer B.')
        return self.build()


def create(computer_type):
    # create request for building
    # factory method
    if computer_type == 'A':
        order = computerA(computer_type)
    elif computer_type == 'B':
        order = computerB(computer_type)
    else:
        print("You are buying the wrong computer!")
        exit(0)
    order.buy()


if __name__ == '__main__':
    computer_type = raw_input("Which Computer you'd like to buy? [A or B]")
    create(computer_type)
