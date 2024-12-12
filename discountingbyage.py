age=int(input("Give your age:"))

if age>=18:
    print("You can enter")

    if age>60:
        print("Discount is available")
    else:
        print("Discount is not available")

else:
    print("You are too young to enter")