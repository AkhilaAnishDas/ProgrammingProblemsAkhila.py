d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"x": 2, "y": 3, "z": 5}

all_values = set(d1.values()) | set(d2.values())

print("Unique values count:", len(all_values))
