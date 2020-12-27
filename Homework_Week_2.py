FirstName = input("Enter your Name: ")
LastName = input("Enter your Lastname: ")
Age = int(input("Enter your Age: "))
Year = int(input("Enter your birth year: "))

list = [FirstName, LastName, Age, Year]

for i in list:
    print(i)

if 2020-Year >= 18:
    print("You can go out to the streets.")
else:
    print("You can't go outside its too dangerous.")
