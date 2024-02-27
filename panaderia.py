eleccionPrincipal = input("Escoja cual producto deseas: bebidas, quesos, postres, ") 
if eleccionPrincipal == "bebidas":
    productosBebidas = tuple((
    "Coca-Cola", 
    "Cafe", 
    "Sprite", 
    "Fanta", 
    "7UP", 
    "Colombiana", 
    "Chocolate", 
    "Tinto", 
    "Limonada", 
    "Naranjada",
    "promocion cafe con sprite",
    "promocion naranjada con tinto, "))

    precios = tuple((
    2500, 
    3000,
    3500, 
    4000, 
    5250, 
    2000, 
    3000, 
    1500, 
    4000, 
    5000,
    5500,
    5500 ))
    for i,val in enumerate(productosBebidas): 
        print(f""" {i}. {val} ${precios[i]}""")

    opcion = int(input())
    print(f"usuario usted selecciono el producto {productosBebidas[opcion]}con un valor de ${precios[opcion]}")
    dinero = int(input("ingrese la cantidad de precio disponible $"))
    vueltos = dinero - precios [opcion]
    if dinero >= precios [opcion] :
        print(f"usuario usted compro el producto {productosBebidas[opcion]} con un valor de $ {precios[opcion]}, sus vueltos son ${vueltos}") 
    else:
        print(f"usuario el prodcuto que desea comprar {productosBebidas[opcion]} con un valor de ${precios[opcion]}, le falta un total de ${-vueltos} ")


elif eleccionPrincipal == "postres":
    productosPostres = tuple((
    "Cake", 
    "PayDeLimon", 
    "PayDeMaracuya", 
    "PayDeFresa", 
    "Torta", 
    "Gelatina", 
    "TresLeches", 
    "Lulo", 
    "Coco", 
    "Mango",
    "Promocion de Cake con PayDeLimon",
    "Promocion de coco con mango, "))

    precios = tuple((
    3000, 
    5000,
    5500, 
    6000, 
    5300, 
    4000, 
    3500, 
    3000, 
    4300, 
    4500,
    7000,
    6300, )) 
    for i,val in enumerate(productosPostres): 
        print(f""" {i}. {val} ${precios[i]}""")

    opcion = int(input())
    print(f"usuario usted selecciono el producto {productosPostres[opcion]}con un valor de ${precios[opcion]}")
    dinero = int(input("ingrese la cantidad de precio disponible $"))
    vueltos = dinero - precios [opcion]
    if dinero >= precios [opcion] :
        print(f"usuario usted compro el producto {productosPostres[opcion]} con un valor de $ {precios[opcion]}, sus vueltos son ${vueltos}") 
    else:
        print(f"usuario el prodcuto que desea comprar {productosPostres[opcion]} con un valor de ${precios[opcion]}, le falta un total de ${-vueltos} ")