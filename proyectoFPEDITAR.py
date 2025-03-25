#resistencia del conductor
def resistencia(rho, longitud, area):
    return rho * (longitud / area)
#perdidas del efecto joule
def perdidas(corriente, resistencia):
    return corriente**2 * resistencia
#resistividades comunes
resis = {
    "cobre": 1.68e-8,
    "aluminio": 2.82e-8}
#datos electricos
material = input("Ingrese el material(cobre/aluminio): ").lower()
while not(material in resis):
    print("Material incorrecto, ingresar cobre o aluminio")
    material = input("Ingrese correctamente el material(cobre/aluminio): ").lower()
#para la definicion de unidad de medida para luego pedirte las variables 1= metros 2= pies
unidades= {
    "1": 1 ,
    "2": 0.3048}
#definicion de la unidad de medida
unidad= input("seleccione su unidad de medida 1=metros 2=pies")
while not(unidad in unidades):
    unidad= input("seleccione correctamente su unidad de medida 1=metros 2=pies")
#unidades en metros o pies ya seleccionada
#metros
if unidad == "1":
    longitud = input("Ingresar la longitud del conductor: ")
    while longitud.isalpha() or not(longitud.isnumeric()) or len(str(longitud))==0:
        longitud= input("Ingresar la longitud del conductor: ")
    longitud = float(longitud) * float(unidades["1"])
#pies
elif unidad == "2":
    longitud = input("Ingresar la longitud del conductor: ")
    while longitud.isalpha() or not(longitud.isnumeric()) or len(str(longitud))==0:
        longitud= input("Ingresar la longitud del conductor: ")
    longitud = float(longitud) * float(unidades["2"])
#Haciendo lo mismo para las areas de unidades de uso comun
#1=mm**2 2=kcmill
unidades2= {"1": 1 ,"2": 5.067e-7}
unidad2= input("seleccione su unidad de medida de area 1=mm2 2=kcmill")
while not(unidad2 in unidades2):
    unidad2= input("seleccione correctamente su unidad de medida de area 1=mm2 2=kcmill")
#unidad de area transversal ya seleccionada
#mm2
if unidad2 == "1":
    area = input("Ingresar el area del conductor: ")
    while area.isalpha() or not(area.isnumeric()) or len(str(area))==0:
        area= input("Ingresar el area del conductor: ")
    area = float(area) * float(unidades2["1"])
#kcmill
elif unidad2 == "2":
    area = input("Ingresar el area del conductor: ")
    while area.isalpha() or not(area.isnumeric()) or len(str(area))==0:
        area= input("Ingresar el area del conductor: ")
    area = float(area) * float(unidades2["2"])
corriente = float(input("Ingrese la corriente en amperes: "))
#material ya seleccionado para calculo de resistencia
if material in resis:
    rho = resis[material]
    resistencia = resistencia(rho, longitud, area) 
    print(f"La resistencia del conductor es: {resistencia:.5e} ohms")
#perdidas por el ef. joule
perdidas = perdidas(corriente, resistencia)
print(f"Las pérdidas por efecto Joule son: {perdidas:.2f} watts")
