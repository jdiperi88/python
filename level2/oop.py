class Dog():
    # class object attribute
    species = 'mammal'

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color


myDog = Dog('pitbull', 'green')


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
myc.set_radius(100)


class Animal():
    def __init__(self):
        print('animal created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('eating')


# mya = Animal()

# mya.whoAmI()
# mya.eat()


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('cat Created')

    def bark(self):
        print('woof')


# mycat = Cat()

# mycat.whoAmI()
# mycat.eat()
# mycat.bark()


# SPECIAL METHODS

class Book():

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('book is destroyed')

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


b = Book('python', 'joey', 300)

del b
