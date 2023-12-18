
#for this task i am required to make a program that needs to make use of 'for loops' in order to display the times tables for any number.

num = int(input("Enter any number: "))
print(f"The {num} timestable is:")

for x in range(1, 13):
    
    print(f"{num} x {x} = {num * x}")
    print("")

