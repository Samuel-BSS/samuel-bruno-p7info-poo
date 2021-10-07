def printDecimal(x):
    return str(x)  

def printOctal(x):
    return str(oct(x)).replace("0o","")

def printHexaDecimal(x):
    return str(hex(x)).replace("0x","")

def printBinario(x):
    return str(bin(x)).replace("0b","")

def imprimirTabela():
    print("{:^10s} {:^10s} {:^10s} {:^10s}".format("Decimal","Octal","Hexadecimal","Binario"))
    for i in range(0, 256):
        print("-" * 43)
        print("{:^10s} {:^10s} {:^10s} {:^10s}".format(printDecimal(i),printOctal(i),printHexaDecimal(i),printBinario(i)))

imprimirTabela()