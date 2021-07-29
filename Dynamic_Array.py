import ctypes
class Dynamic_Array(object):
    def __init__(self):
        self.n = 0
        self.cap = 1
        self.array=self.make_array(self.cap)
    def __len__(self):
        return self.n
    def __getitem__(self,index):
        if not 0 <=index< self.n:
            return IndexError("Index Tasmasi")
        return self.array[index]
    def append(self,value):
        if self.n == self.cap:
            self.__resize(2*self.cap)
        self.array[self.n] = value
        self.n += 1
    def __resize(self,new_cap):
        new_array = self.make_array(new_cap)
        for index in range(self.n):
            new_array[index] = self.array[index]
        self.array = new_array
    def make_array(self,new_cap):
        return (new_cap*ctypes.py_object)()

dynamic_array = Dynamic_Array()

dynamic_array.append(10)
dynamic_array.append(20)
#dynamic_array.append(30)
print(dynamic_array[0] , dynamic_array[1])
print(dynamic_array.__len__())