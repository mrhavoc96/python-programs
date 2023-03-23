class student:
    def __init__(self,name,standard):
        self.name=name
        self.standard=standard

    def display(self):
        print("The name: ", self.name)
        print("Standard: ", self.standard,"th")

student1=student('Vijay',12)
student2=student('Ajay',11)
print("\t\tfirst student: ")
student1.display()
print("\t\tsecond student: ")
student2.display()