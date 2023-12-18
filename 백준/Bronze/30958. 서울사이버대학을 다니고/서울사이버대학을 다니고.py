n = input()
string = input()
count = [0] * 26
for i in string:
    if i.islower():
        count[ord(i) - ord("a")] += 1
max_count = max(count)
print(max_count)
