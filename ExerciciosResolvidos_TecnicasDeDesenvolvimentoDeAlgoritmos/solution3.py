
#Declarando e atribuindo peso e Altura.
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: ")) 

# declarando uma variável para armazenar o IMC.
imc = peso / (altura ** 2)

# imprimindo o resultado do IMC.
print(f"O IMC é: {imc:.2f}")