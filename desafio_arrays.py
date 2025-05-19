
lista_usuario1 = ["campera", "remera", "zapatillas", "bufanda"]
lista_usuario2 = ["pantalon", "gorra", "campera", "buzo", "bufanda"]

def es_string(dato):
    return type(dato) == str

productos_en_comun = []
productos_no_coinciden = []


# Productos en común
for i in range(len(lista_usuario1)):
    for j in range(len(lista_usuario2)):
        if es_string(lista_usuario1[i]) == es_string(lista_usuario2[j]):
            productos_en_comun = productos_en_comun + [lista_usuario1[i]]

# Productos que no coinciden
for i in range(len(lista_usuario1)):
    if es_string(lista_usuario1[i]) not in es_string(productos_en_comun):
        productos_no_coinciden = productos_no_coinciden + [lista_usuario1[i]]

for i in range(len(lista_usuario2)):
    if es_string(lista_usuario2[i]) not in es_string(productos_en_comun):
        productos_no_coinciden = productos_no_coinciden + [lista_usuario2[i]]
#==========================================
#Los demas no me salieron mas profes :(
#==========================================
# Mostrar los resultados
print("Productos en común:", productos_en_comun)
print("Productos que no coinciden:", productos_no_coinciden)
