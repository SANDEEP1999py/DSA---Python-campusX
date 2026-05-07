import ctypes
import sys

class MeraList:
    
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)
    
    def __make_array(self,capacity):
        # creating c type array with fixed size and refferential array
        return(capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            # resize
            self.size = self.size * 2
            B = self.__make_array(self.size)
            for i in range(self.n):
                B[i] = self.A[i]
            self.A = B
        self.A[self.n] = item
        self.n = self.n + 1

    def printing_values(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    
    def __getitem__(self, index):

        counter = 0

        for element in self.A:

            if counter == index:
                return element

            counter += 1

        return "IndexError"
    
    # making pop element, this element also delete the last element also
    def pop_function(self):
        
        if self.n == 0:
            return "Empty List"

        value = self.A[self.n - 1]

        self.A[self.n - 1] = None

        self.n -= 1

        return value

    def clear(self):
        self.size = 1
        self.n = 0

    def find(self,value):
        for i in range(self.n):
            if value == self.A[i]:
                return i
        return 'ValueError - Not in the list'
    
    def resize(self):
        self.size = self.size + 4
        B = self.__make_array(self.size)
        for i in range(self.n):
                B[i] = self.A[i]
        self.A = B

    def insert(self, index, value):
        if self.size <= self.n:
            self.resize()
        for i in range(self.n, index, - 1 ):
            self.A[i] = self.A[i - 1]
        self.A[index] = value
        self.n = self.n + 1


    # deleting index values
    def __delitem__(self, index):
        if 0 <= index < self.n:    
            for i in range(index, self.n - 1):
                self.A[i] = self.A[i+1]
            self.n = self.n - 1

    # removing the particular function 
    def remove(self, value):
        pos = self.find(value=value)
        self.__delitem__(pos)
    
if __name__ == "__main__":
    L = MeraList()
    L.append("hello1")
    L.append("hello2")
    L.append("hello3")
    # L.append("hello4")
    print(len(L))
    print(type(L))
    print(L.printing_values())
    print("-----------------------")
    print(L.pop_function())
    print(L.printing_values())
    print(L.find("hello2"))
    print("-------------------------")
    L.append("hello3")
    L.append("hello4")
    L.insert(index=1,value="hello_inserted")
    print(L.printing_values())
    print("--------------------------")
    del L[0]
    print(L.printing_values())
    L.remove("hello4")
    print(L.printing_values())
    print("main run sucessfully")