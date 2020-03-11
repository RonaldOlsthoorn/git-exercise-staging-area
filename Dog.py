

class Dog:

    def __init__(self):
        print("Dog is born")

    def bark(self):
        print("Woof")

    def fetch(self, fetchedObject):
        raise BaseException("Error!! Dog is distracted")
        print("fetched object {}".format(fetchedObject))


if __name__ == '__main__':
    dog = Dog()
    dog.bark()
