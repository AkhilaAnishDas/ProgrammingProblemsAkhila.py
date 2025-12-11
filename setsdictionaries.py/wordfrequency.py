text = input("Enter paragraph: ")
words = text.split()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)
