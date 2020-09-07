
cadena1= "__servidor1"
cadena2= "3servidor"


def afd (entrada):
    estado=0

    for i in range(len(entrada)):
        if estado==0:
            if entrada[i]=="_":
                estado=1
            elif entrada[i]=="3":
                    print("error cadena incorrecta")

        elif estado==1:
            if entrada[i] =="_":
                estado=1
            elif entrada[i]=="s":
                estado=3

        elif estado==3:
            if entrada[i]=="e":
                estado=3
            elif entrada[i]=="r":
                estado=3
            elif entrada[i]=="v":
                estado=3
            elif entrada[i]=="i":
                estado=3
            elif entrada[i]=="d":
                estado=3
            elif entrada[i]=="o":
                estado=3
            elif entrada[i]=="r":
                estado=3
            elif entrada[i]==1:
                estado=4

        elif estado==4:
            estado==4

afd(cadena1)
print("cadena aceptada")

afd(cadena2)


