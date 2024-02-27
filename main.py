productos = tuple((
    "Coca-Cola", 
    "Pepsi", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Mountain Dew", 
    "Dr Pepper", 
    "Schweppes", 
    "Mirinda", 
    "Lift"))
precios = tuple((
    4500, 
    3750, 
    3000, 
    3600, 
    5250, 
    6000, 
    5400, 
    3900, 
    4200, 
    4800))
for i, val in enumerate(productos):
    print(f"""               {i}. {val} ${precios[i]}""")
opcion = int(input())
print(f"usuario usted selecciono el producto {productos [opcion]}con un valor de ${precios[opcion]}")

dinero = int(input("ingrese la cantidad de precio disponible"))
vueltos = dinero - precios [opcion]
if dinero >= precios [opcion] :
  print(f"usuario usted compro el producto {productos[opcion]} con un valor de $ {precios[opcion]}, sus vueltos son ${vueltos}") 
else:
   print(f"usuario el prodcuto que desea comprar {productos[opcion]} con un valor de ${precios[opcion]}, le falta un total de ${-vueltos} ")