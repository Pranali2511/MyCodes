"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
