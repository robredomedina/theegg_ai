# Recibe un entero como argumento, y devuelve el primer número primo y palíndromo
# Uso: python3 palindromo.py 102
# (Devolverá 131)
import sys

num = int(sys.argv[1])

assert(num >= 1 and num < 1000000), "Number must be >=1 and < 1000000"

def check_primo(num):
    for i in range(2,round(num/2)+1):
        if num%i == 0:
            return False
        else:
            continue
    return True

def check_palindromo(num):
    list_num = list(num)
    reversed_num = list(num)
    reversed_num.reverse()
    return list_num == reversed_num

while True:
    if  check_palindromo(str(num)) and check_primo(num):
        print(num)
        break
    num = num +1 






