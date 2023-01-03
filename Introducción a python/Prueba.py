from http.client import HTTP_VERSION_NOT_SUPPORTED


how_many_snakes = 1
snake_string = """
Welcome to Python3!

             ____
            / . .\\
            \  ---<
            \  /
   __________/ /
-=:___________/

<3, Juno 
"""  # type:ignore

print(snake_string * how_many_snakes)
# ----------------------------------------------------------------

name = input("Enter your name: ")
print("Hello", name.title())

names = input("Insert student name: ").title().split(",")
assignments = (input("Insert number of missing assignaments: ")).split(",")
grades = (input("Insert current grade: ")).split(",")

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
# -----------------------------------------------------------------------------------------------------------------------------


class BankAcount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


per1 = BankAcount("Julio", 200)
per2 = BankAcount("Helio", 400)
# Object Oriented Programming
per1.display()
per2.display()

per1.deposit(200)
per2.withdraw(100)

per1.display()
per2.display()

print(per1.balance, per2.balance)
# ------------------------------------------------------------------------------------------
