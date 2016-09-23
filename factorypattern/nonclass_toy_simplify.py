'''
  This is an example code for a toy factory..
  Creating a factory that could build duck mold and car mold and then injecting the toy mold to finish the create process.
'''


if __name__ == '__main__':
    toy_type = raw_input("Which Toy you'd like to create? [duck or car]")
    if toy_type == "duck":
        # duck_method, each print represent for a process
        color = "Yellow"
        print('{} {} mold is building.'.format(color, toy_type))
        print('{} {} is injecting...'.format(color, toy_type))
        print('Finished.')
        pass
    elif toy_type == "car":
        # car_method, each print represent for a process
        size = "Small"
        print('{} {} mold is building.'.format(size, toy_type))
        print('{} {} is injecting...'.format(size, toy_type))
        print('Finished.')
        pass
    else:
        print("Toy type error!")


