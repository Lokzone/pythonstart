#Exercise 1: Calculate the multiplication and sum of two numbers

# Given two integer numbers return their product only if the product is equal to or lower than 1000, 
# else return their sum.

def cal_num(num1,num2):
    # 計算兩個數字相乘小於1000返回乘法，否則返回兩數之和
    multiplication = num1 * num2
    if multiplication <= 1000:
        print('兩個數字相乘等於： ', multiplication )
    else:
         print('兩個數字相加等於： ', num1+num2)



num1 = int(input("請輸入第一個整數，"))
num2 = int(input("請輸入第二個整數，"))
cal_num(num1,num2)