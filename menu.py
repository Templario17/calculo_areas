#!/usr/bin/env python
#-*- condig: utf-8 -*-

menu = "menu.txt"
banner = "banner.txt"

def leer_banner(banner):
    with open(banner, "r")as archivo:
        banner = archivo.read()
    return banner

print "Script para determinar areas de figuras geometricas"
print leer_banner(banner)

with open(menu, 'r') as archivo:
    menu = archivo.read().split('\n')

for option in menu:
    print "\t", option

opcion_elegida = raw_input("ELIJE UNA OPCION: " )

if opcion_elegida == "1":
    import modulos.areas
elif opcion_elegida == "2":
    print "radio o diametro"
    import modulos.circulo
elif opcion_elegida == "3":
    import modulos.trinagulo
elif opcion_elegida == "4":
    import modulos.rectangulo
elif opcion_elegida == "5":
    print "[*] ha salido correctamente."
else :
    print "[!] Elige la opcion CORRECTA  ..."
