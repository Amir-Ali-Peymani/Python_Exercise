class Person:
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.passowrd = ""
    def loging(self, password):
        if self.passowrd == password:
            return True
        else:
            return False
persons_list = []
person = Person()
name = input("name: \n")
last_name = input("last_name: \n")
password = input("password: \n")
person.name =name
person.last_name =last_name
person.passowrd = password
persons_list.append(person)
print("you have successfully enlisted")

loging_password = input("give your password: ")

# Check if any person in the list has the matching password
for person in persons_list:
    if person.loging(loging_password):
        print("Login successful!")
    else:
        print("Login failed!")