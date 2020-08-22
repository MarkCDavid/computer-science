largest = None
smallest = None
while True:
    user_input = input("Enter a number: ")
    if user_input == "done" : break
    try:
        number = int(user_input)
    except:
        print("Invalid input")
        continue
    
    if largest is None or largest < number:
        largest = number

    if smallest is None or smallest > number:
        smallest = number


print("Maximum is", largest)
print("Minimum is", smallest)