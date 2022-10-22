#ASSIGNMENT 1 - Creating a program that will print my nickname using asterisk character.
#My nickname is 'LEN'

print("\n********PROGRAMMED BY:********")
print("***BEVERLY ANN L. RODRIGUEZ***\n")

letter_L = [[" " for column in range(5)] for int_row in  range(5)]
letter_E = [[" " for column in range(5)] for int_row in  range(5)]
letter_N = [[" " for column in range(5)] for int_row in  range(5)]

#This is for letter L
for row in range(5):
    for col in range(5):
        if col == 0 or (row == 4 and col>0):
            letter_L[row][col] = "*"

#This is for letter E
for row in range(5):
    for col in range(5):
        if (col == 0 or (row == 0 or row == 2 or row == 4) and (col > 0)):
            letter_E[row][col] = "*"

#This is for letter N
for row in range(5):
    for col in range(5):
        if col==0 or col==4 or (row==col and (col>0 and col<4)):
            letter_N[row][col] = "*"


for column in range (5):
    for int_row in range(5):
        print(letter_L[column][int_row], end = "")
    print(end = "  ")
    for int_row in range(5):
        print(letter_E[column][int_row], end = "")
    print(end = "  ")
    for int_row in range(5):
        print(letter_N[column][int_row], end = "")
    print()