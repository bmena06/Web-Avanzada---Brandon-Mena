productos = [
    {
        "id": 123,
        "nombre": "libreta",
        "precio": 12.500,
        "id_cat": 1
    },
    {
        "id": 345,
        "nombre": "Jabon",
        "precio": 10.500,
        "id_cat": 2
    }
]

categorias = [
    {
        "id": 1,
        "nombre": "Utiles escolares"
    },
    {
        "id": 2,
        "nombre": "Aseo"
    }
]

DiccionarioResultante = []

for producto in productos:
    for categoria in categorias:
        if producto["id_cat"] == categoria["id"]:
            producto_info = {
                "id": producto["id"],   
                "nombre": producto["nombre"],
                "categoria": categoria["nombre"]
            }
            DiccionarioResultante.append(producto_info)
            break

print(DiccionarioResultante)
