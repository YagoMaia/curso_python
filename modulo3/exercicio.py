"""
Exercício: Loop de Validação

O objetivo é criar um script onde o usuário deve digitar um número.
O programa deve continuar solicitando a entrada (não parar) até que
o número digitado seja igual ao número correto predefinido.
"""

numero_correto = 10
palpite = -1

while (palpite != numero_correto):
    palpite = int(input("Digite o número: ")) # Str


    # if palpite == numero_correto:
        # break
    print(f"Seu palpite atual foi : {palpite}. Esse não seria o número correto")

print("Você digitou o número correto, meus parabéns.")

# qts_

for qts_palpite in range(1, 4):
    palpite = int(input("Digite o número: ")) # Str


    if palpite == numero_correto:
        print("Você digitou o número correto, meus parabéns.")
        break
    if qts_palpite == 3:
        print("Você não conseguiu acertar o número.")
        break
        
    print(f"Seu palpite atual foi :{palpite}. Esse não seria o número correto")
    print(f"Sua tentativa atual é {qts_palpite}, faltam {3 - qts_palpite}")





