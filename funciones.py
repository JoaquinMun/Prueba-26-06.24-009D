import json
def AgergarCategoria(nombre:str):
    with open("biblioteca.json","r") as archivoAgregarCategoria:
        leerAgregarCategoria = json.load(archivoAgregarCategoria)

        nuevaCategoria ={
            "CategoriaID":len(leerAgregarCategoria["Categoria"]) +1,
            "Nombre":nombre
        }
        leerAgregarCategoria["Categoria"].append(nuevaCategoria)
    with open("biblioteca.json","w") as archivoAgregarCategoria:
        json.dump(leerAgregarCategoria,archivoAgregarCategoria,indent=4)
       
import json
def EliminarCategoria(idCategoriadel:int):
    with open("biblioteca.json","r") as archivoEliminarCategoria:
        leerEliminarCategoria = json.load(archivoEliminarCategoria)
        contador = 0
        for i in leerEliminarCategoria["Categoria"]:
            if i["CategoriaID"] == idCategoriadel:
                del leerEliminarCategoria["Categoria"][contador]
                break
            contador += 1
    with open("biblioteca.json","w") as archivoEliminarCategoria:
         archivoEliminarCategoria.truncate()
         json.dump(leerEliminarCategoria,archivoEliminarCategoria,indent=4)

def EditarCategoria(idCategoriaEdi,nombre):
    with open("biblioteca.json","r") as archivoEditarCategoria:
        leerEditarCategoria = json.load(archivoEditarCategoria)
        contador = 0
        for i in leerEditarCategoria["Categoria"]:
            if i["CategoriaID"] == idCategoriaEdi:
                print("Encontrado")
                break
            contador += 1

        leerEditarCategoria["Categoria"][contador]["Nombre"] = nombre
    with open("biblioteca.json","w") as archivoEditarCategoria:
         json.dump(leerEditarCategoria,archivoEditarCategoria,indent=4)






        
        


        

        