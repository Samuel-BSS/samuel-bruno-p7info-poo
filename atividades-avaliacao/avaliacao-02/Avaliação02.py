def linhas(tamanho_linha):
    for h in range(0,tamanho_linha + len("Maior Palavra: ")):
        print('*',end = "")

frases = ""
frase_parcial = ""
saida = ""
maior_palavra = ""
recent_frase = input("Insira Uma Frase...\n")

while recent_frase != "0":
    if(frases == ""):
        frases = recent_frase
        recent_frase = input("Nova Frase\n")        
    else:
        frases =  frases + "|" + recent_frase
        recent_frase = input("Nova Frase\n")
    
frases_tamanho = frases.replace(" ","-") + "|"

for x in frases_tamanho:
    if x != "-" and x != "|":
        frase_parcial = frase_parcial + x   
    else:
        if x == "-":
            saida = saida + str(len(frase_parcial)) + "-"
            frase_parcial = ""
        else:
            saida = saida + str(len(frase_parcial)) + "|"
            frase_parcial = ""

frases = frases.replace(" ","|")
frases = frases.split("|")
for z in frases:
    if maior_palavra == "":
        maior_palavra = z
    elif len(z) > len(maior_palavra):
            maior_palavra = z

new_saida = saida.split("|")
new_saida.pop()

#Saída "Formatada"............................
linhas(len(maior_palavra))
print("")
print("Saida")
linhas(len(maior_palavra))
print("")
for j in new_saida:
    print(j)
linhas(len(maior_palavra))
print("\nMaior Palavra: "+maior_palavra)
linhas(len(maior_palavra))
