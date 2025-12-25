class Mammal:
    def Walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_adorable(self):
        print('adorable')

dog1 = Dog
dog1.Walk

cat1 = Cat
cat1.be_adorable