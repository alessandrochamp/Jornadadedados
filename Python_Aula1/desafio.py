CONSTANT_BONUS = 1000

# 1 Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário 
# Converta a entrada para um número de ponto flutuante
salario_usuario = float(input("Digite o seu Salário: "))

# 3) Solicita ao usuário que digite o valor do bonus recebido 
# Converta a entrada para um número de ponto flutuante
bonus_usuario = float(input("Digite o valor do bônus: "))


# 4) Calcule o valor de bônus final
valor_do_bonus = CONSTANT_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor 
print(f"O usuario {nome_usuario} possui o bonus de {valor_do_bonus} ")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
