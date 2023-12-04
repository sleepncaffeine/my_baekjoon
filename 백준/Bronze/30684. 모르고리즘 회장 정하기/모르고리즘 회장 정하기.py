def find_president(names):
    three_letter_names = [name for name in names if len(name) == 3]

    three_letter_names.sort()

    return three_letter_names[0]


n = int(input())
names = [input() for _ in range(n)]

president = find_president(names)
print(president)
