class car:
    def __init__(self,name,cost):
        self.name=name
        self.cost=cost
    def display(self):
        print("The name of the car is: ",self.name)
        print("The cost of the car is: ",self.cost)
    
car1=car('BMW A6', 5000000)
car2=car('Mercedees C class', 6000000)

print("\t\tFirst Car: ")
car1.display()

print("\n\t\tSecond Car: ")
car2.display()


