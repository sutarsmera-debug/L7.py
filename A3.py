print("Enter Marks Obtained by 5 Subject:")
markOne = int(input("Enter marks for Math: "))
markTwo = int(input("Enter marks for english: "))
markThree = int(input("Enter marks for Science: "))
markFour = int(input("Enter marks for SS: "))
markFive = int(input("Enter maks for Orchestra: "))

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)
validRange = range(0,101)
if avg not in validRange:
    print("Ivalid Input!")

elif avg in range(80, 101):
    print("Your grade is A")

elif avg in range(65, 80):
    print("Your grade is B")

elif avg in range(41, 65):
    print("Your grade is C")

else:
    print("Fail")