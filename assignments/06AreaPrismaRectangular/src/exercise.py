def area(base,altura):
    return base*altura

def area_prisma(base,altura,profundidad):
    return area(base,altura)*2+area(altura,profundidad)*2+area(base,profundidad)*2

def main():
    #escribe tu código abajo de esta línea
    base = float(input("Dame la base: "))
    altura = float(input("Dame la altura: "))
    profundidad = float(input("Dame la profundidad: "))

    area(base,altura)

    r = area_prisma(base,altura,profundidad)

    print("El área total del prisma es:",+r)

if __name__=='__main__':
    
    main()
