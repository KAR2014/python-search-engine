#coding: utf-8
"""Motor de Busqueda"""
import re
import shutil
import os
import sys
import time
import urllib

#cont = 0
class Motor(object):

    def busqueda(self):
        RESPUESTA = "si"
        while RESPUESTA != "no":

            print "Hola Bienvenido al\n                  ***** Motor de Busqueda ***** \n"

            pagina1 = raw_input("Ingrese #1 URL: ")


            pagina2 = raw_input("Ingrese #2 URL: ")

            palabra = raw_input("Ingrese Palabra a Buscar: ")

            bus1 = urllib.urlopen (pagina1)
            res1 = bus1.read()
            cont1 = len(re.findall(palabra, res1))

            bus2 = urllib.urlopen (pagina2)
            res2 = bus2.read()
            cont2 = len(re.findall(palabra, res2))

            self.pagina1 = pagina1
            self.pagina2 = pagina2
            self.palabra = palabra
            self.bus1 = bus1
            self.res1 = res1
            self.cont1 = cont1
            self.bus2 = bus2
            self.res2 = res2
            self.cont2 = cont2


            if cont1 > cont2:
                print "\nTu Palabra: "+palabra
                print "Aparece en URL #1: "+str(cont1)+" veces"
                print "Aparece en URL #2: "+str(cont2)+" veces"
                print "Página Recomendada: "+pagina1 +"\n"

            elif cont2 > cont1:
                print "\nTu Palabra: "+palabra
                print "Aparece en URL #1: "+str(cont1)+" veces"
                print "Aparece en URL #2: "+str(cont2)+" veces"
                print "Página Recomendada: "+pagina2 +"\n"
            elif (cont1 > 0) and (cont2 > 0) and cont1 == cont2:
                print "Tu Palabra: "+palabra
                print "Aparece en URL #1: "+str(cont1)+" veces"
                print "Aparece en URL #2: "+str(cont2)+" veces"
                print "No hay Página Recomendada"
            elif cont1 == 0 and cont2 == 0:
                print "\nPalabra No Encontrada"
                print "No hay Página Recomendada\n"

            while RESPUESTA != "no":
                RESPUESTA = raw_input("Desea realizar otra busqueda si/no: \n")
                RESPUESTA = RESPUESTA.lower()

                try:
                    RESPUESTA = float(RESPUESTA)
                    RESPUESTA = int(RESPUESTA)
                    print "Error Desea realizar otra busqueda: \n"
                except(RuntimeError, NameError, ValueError):
                    RESPUESTA = RESPUESTA

                if RESPUESTA == "si":
                    pagina1 = ""
                    pagina2 = ""
                    palabra = ""
                    time.sleep(1)
                    os.system("clear")

                    break

                elif RESPUESTA == "no":
                    break

                else:
                    print"\n  Error debe ingresar una opción válida\n"
        raw_input("Presione Enter para continuar ...")
        os.system("clear")
        return

def Menu():
    OP = 0
    while True:
        while (OP != 1)or(OP != 2):

            print"                    ***** Motor de Busqueda © ***** \n"
            print "1. Ingresar Busqueda"
            print "2. Salir"

            OP = raw_input("Ingresa una opción: ")

            try:
                OP = int(OP)
                if OP > 0 and OP <= 2:
                    break
                else:
                    print "Ingrese opción válida\n"
                    time.sleep(1)
                    os.system("clear")
            except(RuntimeError, TypeError, NameError, ValueError):
                print "Ingrese opción válida\n"
                time.sleep(1)
                os.system("clear")

        if OP == 1:
            inicio = Motor()
            inicio.busqueda()

        if OP == 2:
            print "Saliendo ..."
            time.sleep(2)
            os.system("clear")
            print"                            ***** Motor de Busqueda © ***** \n"
            print u"                      Third Generation Grupo: KAR-FER :\n"
            print u"                                 **************"
            print u"                                 Kevin Herrera"
            print u"                                 **************\n"
            print u"                          KAR_KO,INDUSTRIS Copyright ®"
            time.sleep(1)
            sys.exit()
    OP = 0
    return
Menu() # Llamo a mi funcion Menu


