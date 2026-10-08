# def find_gcf(num1,num2):
#     gcf = 1
#     for i in range(1, num1, +1):
#         if num1 % i == 0 and num2 %i == 0:
#             gcf = i
#     return gcf
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(find_gcf(num1,num2))

# 2 DIFFERENT WAYS TO DO GCF UP OR DOWN

def greatest_common_factor(num1,num2):
    a = abs(num1)
    b = abs(num2)

    while b != 0:
        a, b = b, a % b

    return a

num1 = int(input("Whats the first number?"))
num2 = int(input("Whats the second number?"))
print(greatest_common_factor(num1,num2))