class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks   # list of marks

    def average(self):
        return sum(self.marks) / len(self.marks)


# Example
s1 = Student("Akhila", 101, [85, 90, 80])
print("Average:", s1.average())