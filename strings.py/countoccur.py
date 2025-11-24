text = input("Enter a string: ")
ch = input("Enter the character to count: ")

count = 0

for c in text:
    if c == ch:
        count += 1

print("Occurrences:", count)
