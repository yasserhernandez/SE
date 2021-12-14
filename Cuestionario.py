from os import system
print("Cuestionario")
forma = int(input("""¿Que forma tiene el hongo?\n1)Praguas\n2)Trompeta\n3)Plano\n4)Conico\n """))
forma1 = ["Paraguas","Trompeta","Plano","Conico"]
system("cls")
color = int(input("""¿De que color es?\n1)Blancos\n2)Cafe\n3)Rojo\n4)Negro\n5)Verde\n6)Amarillo\n  """))
color1 = ["Blanco","Cafe","Rojo","Negro","Verde","Amarillo"]
system("cls")
otro  = int(input("""¿Tiene algun otro color?\n1)Si\n2)No\n"""))
system("cls")
if otro == 1:
    color2 = int(input("""¿Cual es el segundo color?\n1)Blancos\n2)Cafe\n3)Rojo\n4)Negro\n5)Verde\n6)Amarillo\n """))
    color3 = ["Blanco","Cafe","Rojo","Negro","Verde","Amarillo"]
system("cls")
manchas  = int(input("""¿Tiene manchas?\n1)Si\n2)No\n"""))
manchas1 = ["Si", "No"]
system("cls")
tamaño = int (input("""¿Que tamaño tiene?\n1)Muy pequeño(1-2cm)\n2)Pequeño(2-5cm)\n3)Mediano(5-7cm)\n4)Grande(7-10cm)\n """) )
tamaño1 = ["Muy pequeño","Pequeño","Mediano","Grande"]
system("cls")
ecosistema = int(input("""¿En que tipo de ecosistema lo encontro?\n1)Bosque\n2)Selva\n"""))
ecosistema1 = ["Bosque","Selva"]
system("cls")
ubicacion = int(input("""¿Lo encontro en la tierra o en algun arbol?\n1)En Tierra\n2)En Arbol\n"""))
ubicacion1 = ["En Tierra", "En Arbol"]
system("cls")
print("La informacion recabada es:\nForma de {}\nEl color es {} con {}\n{} Tiene manchas\nTiene un tamaño {}\nSe encuentra en un ecosistema de  {}\nFue encontrado {}".format(forma1[forma-1],color1[color-1],color3[color2-1],manchas1[manchas-1],tamaño1[tamaño-1],ecosistema1[ecosistema-1],ubicacion1[ubicacion-1]))

