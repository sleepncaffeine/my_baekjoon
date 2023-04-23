t = int(input())
for _ in range(t):
    sounds = input().split()
    while True:
        a_goes_b = input()
        if a_goes_b == "what does the fox say?":
            break
        else:
            notfox_sound = a_goes_b.split()[2]
            while notfox_sound in sounds:
                sounds.remove(notfox_sound)
    print(" ".join(sounds))
