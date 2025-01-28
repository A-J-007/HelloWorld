stars = "*"
for i in range(1, 9):
    if i <= 4:
        print(stars)
        stars = stars + "*"
    else:
        print(stars)
        stars = stars[:-1]
print("*")