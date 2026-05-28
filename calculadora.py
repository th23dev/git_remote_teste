num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite a opção (1/2/3/4): "))

if opcao == 1:
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
elif opcao == 2:
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif opcao == 3:
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif opcao == 4:
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")

print("Finalizando programa...)
