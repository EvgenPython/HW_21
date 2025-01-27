# # a, b = b,a
# a = int(input("A "))
# b = int(input("B "))
# while a > b:
#     a = int(input("A "))
#     b = int(input("B "))
#     if a < b:
#         break
#     else:
#         print("Error range")
# num = int(input('N '))
# while b < num or num < a:
#     print("Number not in range")
#     num = int(input('N '))
#     if a < num < b:
#         break
#
# for i in range(a, b + 1):
#     if i != num:
#         print(i, end=" ")
#     else:
#         print(f"|{i}|", end=" ")

min_num, max_num, suma = 0, 0, 0
while True:
    a = int(input("A "))
    if min_num > a:
        min_num = a
    if max_num < a:
        max_num = a
    suma += a
    if a == 7:
        print("Good bay!")
        break
print(f"Min {min_num}, Max {max_num}, Suma {suma}")

