
#For this task I am supposed to create a loop that will count down from 20 to 0.
print("Example 1: ")
for x in range(20 + 1):
    for y in range (0, 21):
        minus = (f"{y} - {x}  = {y-x}")
    print(f"{y-x}")

print("Example 2: ")
#For this task I am required to create a loop that will display all the evn numbers between 1 and 20
for x in range(1, 20):
    if x % 2 == 0:
        print(x)

print("Example 3: ")
#for this task I am required to create a loop that will produce stars from 1 to 5.
for i in range(1,6):
    for j in range (1, i+1):
        print("*", end = "")
    print()
    

print("Example 4: ")
#For this task i am required to write a code that will compute the HCF and 2 possible integers.

g = int(input("Enter the first integer: "))
h = int(input("Enter second integer: "))

#This will be the code to compute the HCF.
while h != 0:
    g, h = h , g % h

print("HCF of the 2 integers given is:  ",g)


