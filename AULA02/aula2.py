idade = int(input("Digite a idade: "))

if idade <= 17:
   print("Você é criança")
elif idade < 60:
   print("Adulto")
else:
   print("Idoso")

######################################################

   for numero in range(1, 51):
      if numero % 2 == 0:
         soma = soma + numero
         print("A soma dos números pares é: ", soma)

######################################################

numero = int(input("Digite um número: "))

for i in range(1,11):
   resultado = numero * i
   print(numero, "x", i,  "=", resultado)