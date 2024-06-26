import json, os ,funciones as fn
while True:
    print("""
    *************************
    *      Mundo Libro      *
    *************************
    1)Mantenedor de Categorias
    2)Reportes
    3)Salir            
    """)
    opcionMundoLibro=int(input("-"))

    if opcionMundoLibro == 1:
        os.system("cls")
        while True:
            print("""
        1)Agregar Categoria
        2)Eliminar Categoria      
        3)Editar Categoria      
        4)Buscar Categoria      
        5)Volver     
                    """)
            
            opcionMantenedorCategoria = int(input("-"))

            if opcionMantenedorCategoria == 1:
                os.system("cls")
                print("Porfavor evitar tildes(á-é-í-ó-ú) y evitar la letra -Ñ-")
                nombre =input("Que nueva Categoria desea ingresar?-")
                fn.AgergarCategoria(nombre)
                print("Creado correctamente")
            elif opcionMantenedorCategoria == 2:
                os.system("cls")
                idCategoriadel =int(input("Deme la categoria que desea eliminar"))
                fn.EliminarCategoria(idCategoriadel)
                os.system("cls")
                print("Eliminado correctamente")
            elif opcionMantenedorCategoria == 3:
                print("Porfavor evitar tildes(á-é-í-ó-ú) y evitar la letra -Ñ-")
                idCategoriaEdi=int(input("Cual es la id que desea Editar?-"))
                nombre=input("porque categoria lo desea remplazar?-")
                fn.EditarCategoria(idCategoriaEdi,nombre)
                os.system("cls")
                print("Editado correctamente")
            elif opcionMantenedorCategoria == 4:
                with open("biblioteca.json","r") as archivoEncontrarCategoria:
                    leerEncontarCategoria = json.load(archivoEncontrarCategoria)
                    for encontrar in leerEncontarCategoria["Categoria"]:
                        print(encontrar)
                        
                 
                os.system
            elif opcionMantenedorCategoria == 5:
                break     
    elif opcionMundoLibro == 2:
         with open("biblioteca.json","r") as archivoConteoCategorias:
            leerConteoCategoria = json.load(archivoConteoCategorias)
            idlibro1 =0
            idlibro2 =0
            idlibro3 =0
            idlibro4 =0
            idlibro5 =0
            idlibro6 =0
            idlibro7 =0
            idlibro8 =0
            idlibro9 =0
            idlibro10 =0
            idlibro11 =0
            idlibro12 =0
            idlibro13 =0
            idlibro14 =0
            idlibro15 =0
            idlibro16 =0
            idlibro17 =0
            idlibro18 =0
            idlibro19 =0
            idlibro20 =0
            for conteo in  leerConteoCategoria["Prestamo"]:
                if conteo["LibroID"] == 1:
                    idlibro1+=1
                elif conteo["LibroID"] == 2:
                    idlibro2+=1
                elif conteo["LibroID"] == 3:
                    idlibro3+=1
                elif conteo["LibroID"] == 4:
                    idlibro4+=1
                elif conteo["LibroID"] == 5:
                    idlibro5+=1
                elif conteo["LibroID"] == 6:
                    idlibro6+=1
                elif conteo["LibroID"] == 7:
                    idlibro7+=1
                elif conteo["LibroID"] == 8:
                    idlibro8+=1
                elif conteo["LibroID"] == 9:
                    idlibro9+=1
                elif conteo["LibroID"] == 10:
                    idlibro10+=1
                elif conteo["LibroID"] == 11:
                    idlibro11+=1
                elif conteo["LibroID"] == 12:
                    idlibro12+=1
                elif conteo["LibroID"] == 13:
                    idlibro13+=1
                elif conteo["LibroID"] == 14:
                    idlibro14+=1
                elif conteo["LibroID"] == 15:
                    idlibro15+=1
                elif conteo["LibroID"] == 16:
                    idlibro16+=1
                elif conteo["LibroID"] == 17:
                    idlibro17+=1
                elif conteo["LibroID"] == 18:
                    idlibro18+=1
                elif conteo["LibroID"] == 19:
                    idlibro19+=1
                elif conteo["LibroID"] == 20:
                    idlibro20+=1
                
                
            print(f"""
                Cien Años de Soledad--------{idlibro1}
                La Casa de los Espíritus--------{idlibro2}
                Rayuela--------{idlibro3}
                La Ciudad y los Perros--------{idlibro4}
                La Sombra del Viento--------{idlibro5}
                Ficciones--------{idlibro6}
                Don Quijote de la Mancha--------{idlibro7}
                Veinte Poemas de Amor y una Canción Desesperada--------{idlibro8}
                Bodas de Sangre--------{idlibro9}
                El Laberinto de la Soledad--------{idlibro10}
                El Amor en los Tiempos del Cólera--------{idlibro11}
                Eva Luna--------{idlibro12}
                Bestiario--------{idlibro13}
                La Fiesta del Chivo--------{idlibro14}
                El Juego del Ángel--------{idlibro15}
                El Aleph--------{idlibro16}
                Novelas Ejemplares--------{idlibro17}
                Residencia en la Tierra--------{idlibro18}
                La Casa de Bernarda Alba--------{idlibro19}
                Piedra de Sol--------{idlibro20}
                    """)
            Reporte = { 
                "Cien Años de Soledad":idlibro1,
                "La Casa de los Espíritus":idlibro2,
                "Rayuela":idlibro3,
                "La Ciudad y los Perros":idlibro4,
                "La Sombra del Viento":idlibro5,
                "Ficciones":idlibro6,
                "Don Quijote de la Mancha":idlibro7,
                "Veinte Poemas de Amor y una Canción Desesperada":idlibro8,
                "Bodas de Sangre":idlibro9,
                "El Laberinto de la Soledad":idlibro10,
                "El Amor en los Tiempos del Cólera":idlibro11,
                "Eva Luna":idlibro12,
                "Bestiario":idlibro13,
                "La Fiesta del Chivo":idlibro14,
                "El Juego del Ángel":idlibro15,
                "El Aleph":idlibro16,
                "Novelas Ejemplares":idlibro17,
                "Residencia en la Tierra":idlibro18,
                "La Casa de Bernarda Alba":idlibro19,
                "Piedra de Sol":idlibro20,
                }
            with open("Reportes_biblioteca_mundo_libro.json","w") as archivoreporte:
                json.dump(Reporte,archivoreporte,indent=4)
    elif opcionMundoLibro == 3:
        print("hasta luego (surrender)")

               

                 

