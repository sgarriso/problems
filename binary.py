class binaryString():
    num = None
    binary = None
    zero_count = 0
    one_count = 0
    sign = None
    def __init__(self,num):
        self.num = num
        self.set_sign(num)
        binary = self.convert(num)
    def set_sign(self,n):
        if n < 0:
            self.sign = '-'
        elif n >= 0:
            self.sign = '+'
    def count(self,n):
        if n == 0:
            self.zero_count = self.zero_count + 1
        elif n == 1:
             self.one_count = self.one_count + 1
    def convert(self,n):
        # array to store 
    # binary number
        binary = ""
  
    # counter for binary array 
        i = 0

        while (n != 0):  
  
            # storing remainder 
            # in binary array
            result = n % 2
            self.count(result)
            binary =  str(result) + binary
            n = int(n / 2)
            i += 1
        self.binary = binary
a = binaryString(5)
print(a.binary)
        
        
