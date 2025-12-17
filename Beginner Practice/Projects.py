def greet_user( first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print("Welcome Aboard")


print("Start")
greet_user("John", "Smith") 
print("FINISH")



class Mammal:
    def Walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class cat(Mammal):
    def be_adorable(self):
        print("Adorable")