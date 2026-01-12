# try / except

# if der_erro: 

nome = "Raydsjakldjaskldjskaljdklaskldaskldasjkldsakldkasljkldsjaljdkaslj"



idade = input("Qual sua idade: ")

try:
    nova_idade = idade + 10
    
except Exception as error:
    print(f"Deu error: {error}")
    idade = int(idade)
    nova_idade = idade + 10

print(f"Sua nova idade é {nova_idade}")
    

