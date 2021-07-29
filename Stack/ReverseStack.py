class CreateStack:
    def __init__(self):
        self.data = []
    def push(self,item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
    def prnt(self):
        for i in self.data:
            print(i)
def reverse(string):
    n = len(string)
    stack = CreateStack()
    for i in range(n):
        stack.push(string[i])
    new_string = ""    
    for i in range(n):
        new_string += stack.pop()
    print(new_string)
   
   
        
reverse("Buğra")