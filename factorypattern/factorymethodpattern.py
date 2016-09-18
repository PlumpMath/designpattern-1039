'''
  This is an example code for factory method pattern.
'''


class InjectionMold:
    def inject(self):
        # real injection process
        print('Finished.')


class duck(InjectionMold):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print('{} {} mold is building.'.format(self.color, self.name))

    def injecting(self):
        # build duck mold
        print('{} {} is injecting...'.format(self.color, self.name))
        return self.inject()


class car(InjectionMold):
    def __init__(self, name, size):
        self.name = name
        self.size = size
        print('{} {} mold is building.'.format(self.size, self.name))

    def injecting(self):
        # build car mold
        print('{} {} is injecting...'.format(self.size, self.name))
        return self.inject()


def create(toy_type, toy_attr):
    # create request for building mold
    toy = eval(toy_type)(toy_type, toy_attr)
    toy.injecting()

if __name__ == '__main__':
    toy_attr = {'duck': 'color', 'car': 'size'}
    toy_type = raw_input("Which Toy you'd like to create? [duck or car]")
    try:
        toy_attr = raw_input("What's the {} of the {}? ".format(toy_attr[toy_type], toy_type))
        create(toy_type, toy_attr)
    except:
        print("Toy type error!")