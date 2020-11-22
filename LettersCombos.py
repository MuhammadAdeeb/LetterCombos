"""
numberOfObjects = input("How many total objects are there? ")
numberOfObjects = int(numberOfObjects)

uniqueOrSame = input("Are these objects unique of same? ")"""

# ***This code is to calculate how many words can be formed from a number of letters. It provides the right answer
# with repeating letters ***

while True:

    while True:
        numberOfLetters = input("How many letters are there? ")
        if numberOfLetters.isdigit():
            # print("HERE")
            numberOfLetters = int(numberOfLetters)
            break
        else:
            print("Number of letters has to be an int! Try again..")

    lettersRepetition = 0
    if numberOfLetters >= 2:
        while True:
            lettersRepetition = input("How many letters are repeated? ")
            if lettersRepetition.isdigit():
                lettersRepetition = int(lettersRepetition)
                break
            else:
                print("Has to be an int. Try again..")
                continue

    aList = []
    index = 0
    sum = 0
    if lettersRepetition >= 1:
        for i in range(lettersRepetition):
            while True:
                x = input("How many times is no. {} repeating letter repeated? ".format((i+1)))
                if x.isdigit():
                    x = int(x)
                    sum += x
                    aList.append(x)
                    break
                else:
                    print("Repetition has to be an int! Try again..")
                    continue
            # index += 1


    def factorial(n):
        fact = 1
        for temp in range(1, n + 1):
            fact = fact * temp

        return fact

    if sum > numberOfLetters:
        print("There can't be more repetitions than number of letters! Please Try again... \n")
        continue

    top = factorial(numberOfLetters)
    bottom = 1
    for i in aList:
        bottom = bottom * factorial(i)

    # print(x)
    possibility = top/bottom
    print("Total possibilities are ", possibility)
    break
    # else:
    #    print("Illogical input! Please Try Again...\n")

"""
number = input("What number do you want to take the factorial of? ")
number = int(number)

returnFact = factorial(number)
print("The factorial of {} = {}".format(number, returnFact))


if uniqueOrSame == 'same':
    numberOfBoxes = input("How many boxes do you want to put these objects in? ")
    numberOfBoxes = int(numberOfBoxes)

    totalPossibilities =


check = input("Are any of them same? ")
if check == 'yes':
    howMany = input("How many of these objects are repeated? ")
    howMany = int(howMany)

    aList = {}
    for i in range(howMany):

        # indivObjRepeated = input("How many of this specific objects are there? ")
        # indivObjRepeated = int(indivObjRepeated)
"""

