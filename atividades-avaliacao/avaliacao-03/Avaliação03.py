
def Soma_e_Quantidade_de_Numeros_Primos (var):
    quant_primos = 0
    quant_divisores = 0
    dividendo = 0
    soma_primos = 0

    while quant_primos < var:
        for divisor in range(1, dividendo + 1):
            if dividendo % divisor == 0:
                quant_divisores = quant_divisores + 1

        if  quant_divisores == 2:
            soma_primos = soma_primos + dividendo
            quant_primos = quant_primos + 1

        quant_divisores = 0
        dividendo = dividendo + 1

    return print("Soma do Numeros Primos: " + str(soma_primos))

user_var = int(input("Insira um numero:\n"))
Soma_e_Quantidade_de_Numeros_Primos(user_var)