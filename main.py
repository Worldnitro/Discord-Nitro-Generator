import random, string
from colorama import init, Fore
import webbrowser

print("Ele só vai gerar nitro para você, você precisa de verificador para verificá-los encontrá-los on-line.\n")
print("Não permitimos cópias deste gerador, não recomendamos fazer um vídeo nele, vamos retirá-lo.\n")
input("Pressione enter se você concordar com isso, o programa será iniciado\n")


num = input('Insira quantos códigos gerar: ')
charSet = f"{string.ascii_uppercase}{string.digits}{string.ascii_lowercase}"
bigStr = ""

with open("Nitro Codes.txt","w", encoding='utf-8') as file:

    print(f'{Fore.BLUE}Aguarde, gerando para você!')

    for i in range(int(num)):
        bigStr += f'https://discord.gift/{"".join(random.choices(charSet, k = 16))}\n'
        if i % 100_000 == 0:
            file.write(f'{bigStr}\n')
            bigStr = ""


    print(f'{Fore.CYAN}Com sucesso, eles são gerados em Nitro Codes.txt"')
    input("Pressione Enter para fechar!")
