text = input("Enter a string: ")

clean_text = text.replace(" ", "").lower()

is_palindrome = True

for i in range(len(clean_text)):
    if clean_text[i] != clean_text[len(clean_text) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
