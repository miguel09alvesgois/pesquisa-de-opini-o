total_excelente = 0
total_ruim = 0
 
for i in range(1,51):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: ")) 
    opiniao = int(input("Digite sua opiniao: 1-EXCELENTE,2-BOM,3-RUIM: "))

    if opiniao == 1:
        print("Opiniao contabilizada")
        total_excelente += 1 
    elif opiniao == 3:
        print("Opiniao contabilizada")
        total_ruim += 1
    elif opiniao == 2:
        print("Opiniao contabilizada")
    else:
        print("Opiniao invalida") 

print("TOTAL EXCELENTE:", total_excelente)
print("TOTAL RUIM:", total_ruim)