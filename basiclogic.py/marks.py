science = float(input("Enter marks for science: "))
hindi = float(input("Enter marks for hindi: "))  
english = float(input("Enter marks for english: "))
sst= float(input("Enter marks for sst: "))
computer = float(input("Enter marks for computer: "))

total_marks = science + hindi + english + sst + computer
print("Total marks:", total_marks)

average_marks = total_marks / 5
print("Average marks:", average_marks)

percentage = (total_marks / 500) * 100
print("Percentage:", percentage)
