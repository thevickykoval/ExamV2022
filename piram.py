def piram(n):
    k = 1
    vidp = 1
    if n!=1:

        for i in range(n-1):
            k+=1
            vidp += k 
    return vidp

if __name__ == '__main__':
    while True:
        a = int(input("Введіть номер: "))
        print(a," елемент = ", piram(a))
   

