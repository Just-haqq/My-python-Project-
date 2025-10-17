class Person:
    def __innit__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()