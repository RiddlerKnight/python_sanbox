names = []
for _ in range(3):
    new_name = input("Give me a name: ")
    names.append(new_name)

with open("names.txt", 'w') as file:
    for name in names:
        file.write(f"{name}\n")
