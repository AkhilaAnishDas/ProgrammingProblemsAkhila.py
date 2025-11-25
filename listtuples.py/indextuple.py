my_tuple = (1,2,3,4)

user_input = int(input("enter a value to find index :"))
if user_input in list (my_tuple):
    for x in list (my_tuple):
        if x == user_input:
            index = list(my_tuple).index(x)
        print(index)

else:
    print("input number doesn't exists")