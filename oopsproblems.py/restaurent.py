class Restaurant:
    def __init__(self):
        self.menu = {
            "pizza": 200,
            "burger": 100,
            "pasta": 150
        }

    def get_bill(self, order_list):
        total = 0
        for item in order_list:
            if item in self.menu:
                total += self.menu[item]
            else:
                print(item, "not available!")
        print("Total Bill:", total)


# Example
r = Restaurant()
r.get_bill(["pizza", "burger"])
