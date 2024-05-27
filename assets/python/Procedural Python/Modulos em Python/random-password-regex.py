import random
import re

# Definindo as listas de caracteres usando regex
lower_chars = re.findall(r'[a-z]', 'abcdefghijklmnopqrstuvwxyz')
upper_chars = re.findall(r'[A-Z]', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
number_chars = re.findall(r'[0-9]', '0123456789')

# Combinação de todas as listas de caracteres
all_chars = lower_chars + upper_chars + number_chars

# Definindo o tamanho da senha
length = 16

# Gerando uma senha com pelo menos um caractere de cada tipo
password = [
    random.choice(lower_chars),
    random.choice(upper_chars),
    random.choice(number_chars)
]

# Preenchendo o restante da senha com caracteres aleatórios
password += [random.choice(all_chars) for _ in range(length - 3)]

# Embaralhando a lista para garantir que os primeiros três caracteres não estejam em ordem
random.shuffle(password)

# Convertendo a lista de caracteres em uma string
password = ''.join(password)

print(password)
