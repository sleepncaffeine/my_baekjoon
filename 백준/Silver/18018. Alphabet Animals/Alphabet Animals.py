prev = input()
n = int(input())
animals = []
for _ in range(n):
    animals.append(input())

char = prev[-1]

elim = False
valid = None

for animal in animals:
    if animal[0] == char:
        if valid is None:
            valid = animal
        next_char = animal[-1]
        elim = True
        for animal2 in animals:
            if animal2 == animal:
                continue
            if animal2[0] == next_char:
                elim = False
                break
        if elim:
            print(f"{animal}!")
            exit()

if valid is not None:
    print(valid)
else:
    print("?")
