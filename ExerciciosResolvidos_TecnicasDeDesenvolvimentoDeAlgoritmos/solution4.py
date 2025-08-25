#Desconto

#Declarando a variavel "total_compra"
total_compra = float(input("Digite o valor total da compra: "))

#Declarando a variavel "desconto"
desconto = total_compra * 0.10

#Declarando a variavel "valor_final"
valor_final = total_compra - desconto

#Imprimindo o valor final da compra após o desconto.
print(f"O valor final da compra após o desconto é: {valor_final:.2f}")
