class Calculator:

    def __init__(self, memory):
        self.memory = memory

    def add(self, num):
        '''Adds an integer to number in the memory.'''
        self.memory = self.memory + num

    def sub(self, num):
        '''Subtracts an integer to number in the memory.'''
        self.memory = self.memory - num

    def mult(self, num):
        '''Adds an integer to number in the memory.'''
        self.memory = self.memory * num

    def div(self, num):
        '''Divides the number in memory by an integer.'''
        self.memory = self.memory / num

    def root(self, root):
        '''Takes the (n) root of the number in the memory.'''
        self.memory = self.memory**(1/root)

    def get_result(self):
        '''Returns the memory content.'''
        return self.memory

    def clear_memory(self):
        '''Sets the memory to 0.'''
        self.memory = 0
        return self.memory

    def set_memory(self, num):
        '''Sets the memory to the integer provided by user.'''
        self.memory = num
