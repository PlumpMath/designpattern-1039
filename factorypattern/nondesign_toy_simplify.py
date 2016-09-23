'''
  This is an example code for factory method pattern.
  Creating a factory that could build duck mold and car mold and then injecting the toy mold to finish the create process.
'''


class Factory:
    # build duck mold
    def __init__(self, name):
        self.name = name
        pass
    def build(self):
        if self.name == "duck":
            self.color = 'Yellow'
            print('{} {} mold is building.'.format(self.color, self.name))
        elif self.name == "car":
            self.size = 'Small'
            print('{} {} mold is building.'.format(self.size, self.name))
    def injecting(self):
        if self.name == "duck":
            print('{} {} is injecting...'.format(self.color, self.name))
        elif self.name == "car":
            print('{} {} is injecting...'.format(self.size, self.name))
        return self.__inject()
    def __inject(self):  # private
        # real injection process
        print('Finished.')

if __name__ == '__main__':
    toy_type = raw_input("Which Toy you'd like to create? [duck or car]")
    toy = Factory(toy_type)
    toy.build()
    toy.injecting()
