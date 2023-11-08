valorUm = float(input("insira um valor "))
valorDois = float(input("insira um segundo valor "))
operação = input("escolha uma das operações soma (+), subtração(-),  multiplicação (*) ou divisão (/) ")

if operação == "+":
    soma = valorUm + valorDois
    print(f"o resuldato da soma de {valorUm} + {valorDois} = {soma}")

else:
    if operação == "-":
        subtração = valorUm - valorDois
        print(f"o resuldato da subtração de {valorUm} + {valorDois} = {subtração}")
    else:
        if operação == "*":
            multiplicação =  valorUm * valorDois
            print(f"o resultado da multiplicação de {valorUm} * {valorDois} = {multiplicação}")
        else:
            if operação == "/":
                divisão =  valorUm / valorDois
                print(f"o resultado da divisão de {valorUm} / {valorDois} = {divisão}")