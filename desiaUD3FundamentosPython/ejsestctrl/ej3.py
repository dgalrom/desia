# Recorre los números del 1 al 15
# Si el número es divisible por 3, imprime "Fizz"
# Si es divisible por 5, imprime "Buzz"
# Si es divisible por ambos, imprime "FizzBuzz"
# Si no, imprime el número

for i in range(1,16):
    if i%3==0:
        print("Fizz")
    
    if i%5==0:
        print("Buzz")
    
    if i%3!=0:
        if i%5!=0:
            print(i)
    

    