def escribir():
    with open("archivo.txt", "w") as archivo:
        archivo.write("hola mundo")
        archivo.write("\nholis")
        archivo.write("\ngalleta")
        archivo.write("\nchao")
escribir()