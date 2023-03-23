class random:
    def __init__(self, name, result):
        self.name=name
        self.result=result
    def display(self):
       return f"name is {self.name} and result is {self.result}" 

vijay=random("vijay",87)
print(vijay.display())
