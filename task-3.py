# Даны три числа. Вывести на экран «yes«, если среди них есть одинаковые, иначе вывести “ERROR”;


a = (input())
# b = int(input())
# c = int(input())


for i in range(3):

    if len(set(a)) == len(a):
        print("ERROR")    
    else:
        print("YES")