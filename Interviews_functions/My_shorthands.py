from re import X
import pandas as pd
import numpy as np

class My_code:
    def Swapping(self,x,y):
        print('Entered x is  and y values are:',x,'and',y)
        x,y = y,x        
        print('Changed x and y values are:',x ,'and',y)

    def Factorial(self,num):
        fact = 1
        for i in range(num,1,-1):
            fact = fact*i
        print("Factorial of ",num,"is",fact)

    def Fibonacci_sum(self,num):
        fno,sno = 0,1
        res = fno + sno
        print(fno)
        print(sno)
        while res <num:
            print(res)
            fno,sno=sno,res
            res=fno+sno
    
    def Is_prime(self,num):
        for i in range(2,num):
            if num%i==0:
                print(num, 'is not a prime')
                break
            else:
              print(num, 'is a prime')
              break  
    
    def Is_palindrome(self,num):
        # Pass any string or number
        str_num=str(num)
        if str_num==str_num[::-1]:
            print(num,'is palindrome')
        else:
            print(num,'is not palindrome')
    
    def Is_armstrong(sef,num):
        num_len=len(str(num))
        res=0
        for i in str(num):
            res_i=int(i)**num_len
            res=res+res_i
            if num==res:
                print(num,'Is Armstrong number')
            else:
                print(num,'Is not Armstrong number')

    def Biggest_numbe(self,list_num):
        # USing Pandas
        df=pd.DataFrame(list_num)
        max_value_of_list=df[0].max()
        print(max_value_of_list,'is the maximum number')
        # Using Numpy
        # array_list=np.array(list_num)
        # max_value_of_list=array_list.max()
        # print(max_value_of_list,'is the maximum number')

    def Finding_element(self,list_num,num):
        # list_num=[1,2,3,4,5,6,'iranna']
        counts=list_num.count(num)
        print('The counts of',num,'=',counts)

    def Removing_duplicates(self,list_num):
        print(list(set(list_num)))

    def Count_vowels(self,string_value):
        vowels=['a','e','i','o','u','A','E','I','O','U']        
        count=0
        for i in string_value:
            if i in vowels:
                count=count+1
        print('Total vowels counts in string=',count)



object1=My_code()
# object1.Swapping(14,17)
# object1.Factorial(5)
object1.Count_vowels('Iranna Hanapur')
