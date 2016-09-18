'''
  This is an example code for factory method pattern.
'''


class InjectionMold:
    def inject(self):
        # real injection process
        print('Finished.')


class duck(InjectionMold):
    def __init__(self, name):
        self.name = name
        self.color = 'Yellow'
        print('{} {} mold is building.'.format(self.color, self.name))

    def injecting(self):
        # build duck mold
        print('{} {} is injecting...'.format(self.color, self.name))
        return self.inject()


class car(InjectionMold):
    def __init__(self, name):
        self.name = name
        self.size = 'Small'
        print('{} {} mold is building.'.format(self.size, self.name))

    def injecting(self):
        # build car mold
        print('{} {} is injecting...'.format(self.size, self.name))
        return self.inject()


def create(toy_type):
    # create request for building
    toy = eval(toy_type)(toy_type)
    toy.injecting()

if __name__ == '__main__':
    toy_type = raw_input("Which Toy you'd like to create? [duck or car]")
    try:
        create(toy_type)
    except:
        print("Toy type error!")