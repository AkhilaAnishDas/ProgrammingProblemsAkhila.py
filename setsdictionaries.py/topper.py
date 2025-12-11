marks = {
    "Akhila": 78,
    "Riya": 92,
    "Karan": 67,
    "Meera": 88,
    "John": 95
}

topper = max(marks, key=marks.get)

print("Topper:", topper, "→", marks[topper])
