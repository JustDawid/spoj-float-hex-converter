def main(): 

    while True:
        wejscie = input("Podaj liczby oddzielone spacjami: ")
        z = dane(wejscie)
        if z is not None:
            break

    print("dec - hex")    
    for liczba in z:
        c = konwersja(liczba)
        print(f"{liczba} to {c}")
    
def dane(wejscie):
    try:
        lista = [float(x) for x in wejscie.replace(",", " ").split()]
        return lista
    except ValueError:
        print("Proszę podać poprawne liczby.")
        return None

def konwersja(liczba):
    hex_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    x = []
    calkowita = int(liczba)
    ulamkowa = liczba - calkowita

    if calkowita == 0:
        x.append("0")
    else:
        while calkowita > 0:
            modulo = calkowita % 16
            x.append(hex_map.get(modulo, str(modulo)))
            calkowita //= 16
        
    x.reverse()
    
    if ulamkowa > 0:
        x.append(".")
        for _ in range(1):
            ulamkowa *= 16
            cyfra = int(ulamkowa)
            x.append(hex_map.get(cyfra, str(cyfra)))
            ulamkowa -= cyfra
            if ulamkowa == 0:
                break

    return "".join(x)

main()