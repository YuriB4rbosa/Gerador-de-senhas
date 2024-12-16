import random
import string

def gerar_senha(tamanho=12):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    caracteres = letras + numeros + simbolos
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


tamanho_senha = int(input("Digite o tamanho da senha: "))


senha_gerada = gerar_senha(tamanho_senha)


print(f"Sua senha gerada é: {senha_gerada}")


