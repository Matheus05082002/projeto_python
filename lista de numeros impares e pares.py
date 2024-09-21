numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
multiplicação = 3
numeros_inteiros = list(map(lambda x: x * multiplicação, numeros))
numeros_pares = list(filter(lambda x: x % 2 == 0 , numeros))
numeros_multiplos_de_3 = list(filter(lambda x: x % 3 == 0 , numeros))
numeros_multiplos_de_4 = list(filter(lambda x: x % 4 == 0 , numeros))
numeros_multiplos_de_5 = list(filter(lambda x: x % 5 == 0 , numeros))
numeros_multiplos_de_10 = list(filter(lambda x: x % 10 == 0 , numeros))
print(numeros_inteiros)
print(numeros_pares)
print(numeros_multiplos_de_3)
print(numeros_multiplos_de_4)
print(numeros_multiplos_de_5)
print(numeros_multiplos_de_10)