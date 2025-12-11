d = {"name": "Akhila", "age": 20, "city": "Pune"}

key = input("Enter key to remove: ")

if key in d:
    d.pop(key)
else:
    print("Key not found")

print(d)
