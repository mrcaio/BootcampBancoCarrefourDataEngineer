a = int(input('Entre com o primeiro valor '))
b = int(input('Entre com o segundo valor 1'))
#a = 10  
#b = 5
soma = a + b
subtracao = a-b
multiplicacao= a*b
divisao= a/b
resto= a%b
# print(soma)
# print(subtracao)
# print(multiplicacao)
# print(divisao)
# print(resto)
# print(type(soma)) #tipo da variavel
# print('soma:' + str(soma)) #conversao da variavel
# print('soma: {}' .format(soma))
resultado= ('soma: {som} \nsubtracao: {sub}' 
        '\nMultiplicação: {mult}' '\nDivisão: {div}'
        '\nResto: {rest}'
        .format(som=soma, sub=subtracao, mult=multiplicacao, div=divisao, rest=resto))
print(resultado)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)