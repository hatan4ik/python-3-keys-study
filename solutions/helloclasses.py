'''

>>> fido = Dog("Fido")
>>> fido.describe()
'Fido the dog says: Woof!'

>>> fifi = Cat("Fifi")
>>> fifi.describe()
'Fifi the kitty cat says: Meow!'

>>> nemo = Fish("Nemo")
>>> nemo.describe()
'Nemo the fish says: '

'''

# Write your code here:

class Pet:
    sound = ''
    species = ''
    def __init__(self, name):
        self.name = name
    def describe(self):
        return self.name + ' the ' + self.species + ' says: ' + self.sound

class Dog(Pet):
    sound = 'Woof!'
    species = 'dog'

class Cat(Pet):
    sound = 'Meow!'
    species = 'kitty cat'

class Fish(Pet):
    species = 'fish'

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# From Powerful Python. Copyright MigrateUp LLC. All rights reserved.
