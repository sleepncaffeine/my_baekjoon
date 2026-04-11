n = int(input())
nums = list(map(int, input().split()))

odds = [x for x in nums if x % 2 == 1]
evns = [x for x in nums if x % 2 == 0]

if len(evns) > len(odds):
    print("Happy")
else:
    print("Sad")