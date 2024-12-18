def is_prime(number):
    k = 0
    for i in range(2,number):
        if number%i == 0:
            k+=1
    if k == 0:
        return F'True'
    else:
        return F'False'
print(is_prime(int(input("Введите число:"))))