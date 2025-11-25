set1 = set(map(int, input("Enter first set numbers separated by space: ").split()))
set2 = set(map(int, input("Enter second set numbers separated by space: ").split()))

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
