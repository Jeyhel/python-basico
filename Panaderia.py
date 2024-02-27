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
    nProductos = int(input("'¿Cuantos productos desea? "))
    print(f"usuario usted selecciono el producto {productosBebidas[opcion]}con un valor de ${precios[opcion]*nProductos}")
    dinero = int(input("ingrese la cantidad de precio disponible $"))
    vueltos = dinero - (precios [opcion]*nProductos)
    if dinero >= precios [opcion]*nProductos :
        print(f"usuario usted compro el producto {productosBebidas[opcion]} con un valor de $ {precios[opcion]*nProductos}, sus vueltos son ${vueltos}") 
    else:
        print(f"usuario el producto que desea comprar {productosBebidas[opcion]} con un valor de ${precios[opcion]*nProductos}, le falta un total de ${vueltos} ")


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
    nProductos = int(input("¿Cuantos productos desea? "))
    print(f"usuario usted selecciono el producto {productosPostres[opcion]}con un valor de ${precios[opcion]*nProductos}")
    dinero = int(input("ingrese la cantidad de precio disponible $"))
    vueltos = dinero - precios [opcion]*nProductos
    if dinero >= precios [opcion]*nProductos :
        print(f"usuario usted compro el producto {productosPostres[opcion]} con un valor de $ {precios[opcion]*nProductos}, sus vueltos son ${vueltos}") 
    else:
        print(f"usuario el producto que desea comprar {productosPostres[opcion]} con un valor de ${precios[opcion]*nProductos}, le falta un total de ${vueltos}")
        
elif eleccionPrincipal == "quesos":  
    productosQuesos = tuple((
    "Cheddar", 
    "Parmesano", 
    "Mozzarella", 
    "Brie", 
    "Manchego", 
    "Camembert", 
    "Roquefort", 
    "Gorgonzola",
    "Emmental", 
    "Feta",
    "Promocion de Brie con Manchego",
    "Promocion de Feta con Emmental, "))

    precios = tuple((
    6000, 
    8000,
    8500, 
    5000, 
    4500, 
    4500, 
    8200, 
    5000, 
    5000, 
    3000,
    9500,
    8000, )) 
    for i,val in enumerate(productosQuesos): 
        print(f""" {i}. {val} ${precios[i]}""")

    opcion = int(input())
    nProductos = int(input("¿Cuantos productos desea? "))
    print(f"usuario usted selecciono el producto {productosQuesos[opcion]}con un valor de ${precios[opcion]*nProductos}")
    dinero = int(input("ingrese la cantidad de precio disponible $"))
    vueltos = dinero - precios [opcion]*nProductos
    if dinero >= precios [opcion]*nProductos : 
        print(f"usuario usted compro el producto {productosQuesos[opcion]} con un valor de $ {precios[opcion]*nProductos}, sus vueltos son ${vueltos}") 
    else:
        print(f"usuario el prodcucto que desea comprar {productosQuesos[opcion]} con un valor de ${precios[opcion]*nProductos}, le falta un total de ${vueltos}")
        
        
        