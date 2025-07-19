import math

# #### Inteiros (`int`)
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 + numero_02
print("A soma dos numeros é: {resultado}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero_01 = int(input("Inserir um numero inteiro: "))
resultado = numero_01 % 5
print("O resto da divisão é: {resultado}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 * numero_02
print("A multiplicação dos números é: {resultado}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_01 = int(input("Inserir um numero inteiro: "))
numero_02 = int(input("Inserir outro numero inteiro: "))
resultado = numero_01 // numero_02
print("A divisão inteira dos números é: {resultado}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero_01 = int(input("Inserir um numero inteiro: "))
resultado = numero_01 * numero_01
print("A divisão inteira dos números é: {resultado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_01 = float(input("Inserir um numero float: "))
numero_02 = float(input("Inserir outro numero float: "))
resultado = numero_01 + numero_02
print("A adição dos números flutuantes é: {resultado}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_01 = float(input("Inserir um numero float: "))
numero_02 = float(input("Inserir outro numero float: "))
resultado = (numero_01 + numero_02)/2
print(resultado)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = int(input("Inserir um numero float: "))
expoente = int(input("Inserir outro numero float: "))
resultado = base ** expoente
print("O resultado do exponencial é: {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = int(input("Inserir a temperatura: "))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura de {celsius} celsius em fahrenheit é: {fahrenheit}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)
# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite um texto: ")
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = input("Digite seu nome completo: ")
nome_minusculas = nome_completo.lower()
print("Nome em minúsculas:", nome_minusculas)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
parte1 = input("Digite a primeira parte do texto: ")
parte2 = input("Digite a segunda parte do texto: ")
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)

data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)
# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação