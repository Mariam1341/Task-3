def check(list, N):
    count = 0
    for i in list:
        if N == 0:
            N = int(input ("Enter another number:  "))
        elif (i % N) == 0:
            print(i)
            count = 1
    if count == 0:
        print("There is no item divisible by",N)

N = int(input ("Enter the number you wanna check:  "))
list = [1, 4, 5, 10, 9]
print("The numbers in", list,"that are divisible by", N,"are:")
check(list, N)




