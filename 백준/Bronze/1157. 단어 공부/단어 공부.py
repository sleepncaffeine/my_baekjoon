word = input().upper()
alphabet_counts = [0] * 26
for ch in word:
    if ch.isalpha():
        alphabet_counts[ord(ch) - ord('A')] += 1 
max_count = max(alphabet_counts)
if alphabet_counts.count(max_count) > 1:
    print("?")
else:
    max_idx = alphabet_counts.index(max_count)
    print(chr(max_idx + ord('A')))