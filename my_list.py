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

    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    
    def __getitem__(self, index):

        counter = 0
        if index < 0:
            index = self.n  + index
        else:
            index = index

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

    # finding minimum values from array
    def minimum(self):
        min_value = self.A[0]
        for i in range(1, self.n):
            if min_value > self.A[i]:
                min_value = self.A[i]
        return min_value
    
    def maximum(self):
        max_value = self.A[0]
        for i in range(1,self.n):
            if max_value < self.A[i]:
                max_value = self.A[i]
        return max_value

    def summation(self):
        sum = 0
        for i in range(self.n):
            sum = sum + self.A[i]
        return sum
    
    def sorting_array(self):
        C_arr = self.__make_array(self.size + 4)
        orignal_n = self.n

        for i in range(orignal_n):
            min_b = self.minimum()
            C_arr[i] = min_b
            self.remove(min_b)

        self.A = C_arr
        self.n = orignal_n
        return [C_arr[i] for i in range(self.n)]


    def extend_arr(self,__arr):
        for i in range(len(__arr)):
            self.append(__arr[i])

    
    def slicing_(self, start, end):
        C_arr = self.__make_array(self.n)
        count = 0
        for i in range(start,end):
            C_arr[count] = self.A[i]
            count = count + 1
        return [C_arr[i] for i in range(count)]
    
    def print_array(self, arr, n):
        return [arr[i] for i in range(n)]
    


# home work is the 
# sort / min / max / sum / extend / negative indexing
# slicing / merge
    
if __name__ == "__main__":

    L = MeraList()
    L.append("hello1")
    L.append("hello2")
    L.append("hello3")
    # L.append("hello4")
    print(len(L))
    print(type(L))
    print(L)
    print("-----------------------")
    print(L.pop_function())
    print(L)
    print(L.find("hello2"))
    print("-------------------------")
    L.append("hello3")
    L.append("hello4")
    L.insert(index=1,value="hello_inserted")
    print(L)
    print("--------------------------")
    del L[0]
    print(L)
    L.remove("hello4")
    print(L)

    arr = MeraList()
    arr.append(10)
    arr.append(5)
    arr.append(90)
    arr.append(2)
    arr.append(1)
    print(arr)
    min_value = arr.minimum()
    print(min_value)
    print(arr.maximum())
    print(arr.summation())
    print(arr.sorting_array())
    print(arr.maximum())
    print(arr)
    print("-------------------------")
    # arr.extend_arr(arr)
    print(arr)
    print(arr[-1])
    print("--------------Slicing")
    C_arr = arr.slicing_(start=1,end=3)
    print(C_arr)
    print("main run sucessfully")