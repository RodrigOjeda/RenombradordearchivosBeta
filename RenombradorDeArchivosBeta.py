import os

# busca y remplaza el nombre con la extencion 
search = "" #Cambiar por nombre de origen de los archivos
replace = "" #Nuevo nombre del archivo
type_filter = "." #Nombre de la extencion .png .jpeg etc

# Obtiene los archivos dentro del directorio
dir_content = os.listdir('.')
docs = [doc for doc in dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} de {len(dir_content)} de los elementos son archivos.")

# Revisa los archivos si coinciden con el patron de busqueda
for doc in docs:
    # separa los nombres por extencion
    doc_name, filetype = os.path.splitext(doc)

    # filtra los nombres por extencion
    if filetype == type_filter:
        # comprueba si el texto esta en el nombre del documento
        if search in doc_name:
            
            #Remplaza el nombre
            new_name = doc_name.replace(search, replace) + filetype
            os.rename(doc, new_name)
            renamed += 1

            print(f"archivos renombrados {doc} to {new_name}")

print(f"archivos renombrados {renamed} de {len(docs)} .")