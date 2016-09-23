'''
  This is an example code for factory method pattern.
  Creating a factory that could build duck mold and car mold and then injecting the toy mold to finish the create process.
'''


class InjectionMold:
    def inject(self):
        # real injection process
        print('Finished.')

class duck(InjectionMold):
    # build duck mold
    def __init__(self, name):
        self.name = name
        self.color = 'Yellow'
        print('{} {} mold is building.'.format(self.color, self.name))
    def injecting(self):
        print('{} {} is injecting...'.format(self.color, self.name))
        return self.inject()

class car(InjectionMold):
    # build car mold
    def __init__(self, name):
        self.name = name
        self.size = 'Small'
        print('{} {} mold is building.'.format(self.size, self.name))
    def injecting(self):
        print('{} {} is injecting...'.format(self.size, self.name))
        return self.inject()

def create(toy_type):
    # create request for building
    # factory method
    try:
        toy = eval(toy_type)(toy_type)
        toy.injecting()
    except:
        print("Toy type error!")

if __name__ == '__main__':
    toy_type = raw_input("Which Toy you'd like to create? [duck or car]")
    create(toy_type)
