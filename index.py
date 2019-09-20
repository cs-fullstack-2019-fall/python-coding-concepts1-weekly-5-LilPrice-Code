def main():
    # pro1()
    # pro2()
    # pro3()
    # pro4()
    # pro5()
    # pro6()
    # pro7()
    # pro8()
    # pro9()
    pro10()

def pro1(): # Ask a user for the year they were born by calculating their age. Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”
    user = int(input("Enter the year you were born?\n"))
    num = 2019 - user
    print(f"You are {num} years old!")

def pro2():
    # Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or “Autumn” print “Hello Teacher”. Otherwise print “Hello Student”
    user = input("Enter a name\n")
    if user == "Kenn" or user == "Kevin" or user == "Erin" or user == "Autumn":
        print("Hello Teacher")
    else:
        print("Hello Student")

def pro3():
    # Ask the user for a negative number. Print from 7 down to the user's negative number. You must include the user's number.
    user = int(input("Enter a negative number?(like -20)\n"))
    num = 7
    while num >= user:
        print(num)
        num-=1

def pro4():
    # Ask the user to enter a number between -10 to -5. If their input is not between the two numbers ask them to do it again until they get it right. Afterward they print the correct number, print "Good job"
    num = 0
    while num == 0:
        user = int(input("Enter a number between -10 to -5\n"))
        if user <= -5 and user >= -10:
            print("Good Job")
            num +=1
        else:
            print("Try Again")

def pro5():
    # Create the list: squad = ["One", "Two", "Three", "Four", "Five"]. Print the list in reverse without using a list method.
    squad = ["One", "Two", "Three", "Four", "Five"]
    for x in range(len(squad)-1, -1, -1):
        print(squad[x])

def pro6():
    # Create a function that will have the string firstName as a parameter. In the function ask the user for their last name. Print "Hello [FIRST & LAST NAME]" in the function. Call that function
    def printname(firstname):
        user = input("What is your last name?\n")
        print(f"Hello {firstname} {user}")
    printname("John")

def pro7():
    # Create the class Books with name, rating, genre, and author properties/attributes. Create a class method that will change the rating of the book. Outside of the class, create three objects of the class Book and put them in an array. Lastly, USING THE ARRAY print only the names of the books using any method we’ve learned in class.
    class Books:
        def __init__(self, name, rating, genre, author):
            self.name = name
            self.rate = rating
            self.genre = genre
            self.author = author

        def changerate(self,rate):
            self.rate = rate


    b1 = Books("Harry", "9/10", 'Fantasy','AuthorA')
    b2 = Books("Jerry", "7/10", 'Action','AuthorA')
    b3 = Books("Barry", "9.9/10", 'Sports','AuthorA')
    bookArray = [b1,b2,b3]
    for x in range(0, len(bookArray)):
        print(bookArray[x].name)

def pro8():
    # Create a function that asks the user to enter a number. If the number is between and include -50 and 5, return "Funds too low". If the number is between 5 and 50, return “You should add more funds.” If the number is more than 50, return “Just enough.”
    def funds():
        user = int(input("Enter a number\n"))
        if user >= -50 and  user <= 5:
            return "Funds too low"
        elif user > 5 and user <= 50:
            return "You should add more funds"
        elif user > 50:
            return "Just enough"

    print(funds())

def pro9():
    # Ask the user for a positive number. Create an empty array and starting from zero, add each number by 1 into the array. Print EACH ELEMENT of the array.
    user = int(input("Enter a positive number\n"))
    num = 0
    number = []
    while num <= user:
        number.append(num)
        num += 1
    for x in number:
        print(x)

def pro10():
    # Create a new empty array called pet_list. Create a Pet class with a type and breed attribute/property. Include a method that will print each attribute/property. Add 3 pet objects to the pet_list array. Print the attributes/properties for each pet.
    pet_list = []
    class Pet:
        def __init__(self,type,breed):
            self.type = type
            self.breed = breed
        def printall(self):
            str = (f"self.type = {self.type} " 
                   f"self.breed = {self.breed}")
            return str

    p1 = Pet("Cat", "Russian Blue")
    p2 = Pet("Dog", "Husky")
    p3 = Pet("Bird", "Parrot")
    pet_list.append(p1)
    pet_list.append(p2)
    pet_list.append(p3)
    for x in range(0, len(pet_list)):
        print(pet_list[x].printall())

main()