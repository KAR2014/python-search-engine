#coding: utf-8
"""Motor de Busqueda"""
import re
import os
import sys
import time
import urllib

#cont = 0
class _Motor(object):
    def __init__(self):
        self.pagina1 = ""
        self.pagina2 = ""
        self.palabra = ""
        self.bus1 = ""
        self.res1 = ""
        self.cont1 = 0
        self.bus2 = ""
        self.res2 = ""
        self.cont2 = 0
        self.oportunidad = 0

    def busqueda(self):
        respuesta = "si"
        while respuesta != "no":

            print "Hola Bienvenido al\n "
            print "***** Motor de Busqueda ***** \n"

            self.pagina1 = raw_input("Ingrese #1 URL: ")
            self.pagina2 = raw_input("Ingrese #2 URL: ")
            self.palabra = raw_input("Ingrese palabra a Buscar: ")

            self.bus1 = urllib.urlopen(self.pagina1)
            self.res1 = self.bus1.read()
            self.cont1 = len(re.findall(self.palabra, self.res1))

            self.bus2 = urllib.urlopen(self.pagina2)
            self.res2 = self.bus2.read()
            self.cont2 = len(re.findall(self.palabra, self.res2))

            if self.cont1 > self.cont2:
                print "\nTu palabra: " + self.palabra
                print "Aparece en URL #1: " + str(self.cont1) + " veces"
                print "Aparece en URL #2: " + str(self.cont2) + " veces"
                print "Página Recomendada: " + self.pagina1 + "\n"

            elif self.cont2 > self.cont1:
                print "\nTu palabra: " + self.palabra
                print "Aparece en URL #1: " + str(self.cont1) + " veces"
                print "Aparece en URL #2: " + str(self.cont2) + " veces"
                print "Página Recomendada: " + self.pagina2 + "\n"

            elif (self.cont1 > 0) and (self.cont2 > 0) and self.cont1 == self.cont2:
                print "Tu palabra: " + self.palabra
                print "Aparece en URL #1: " + str(self.cont1) + " veces"
                print "Aparece en URL #2: " + str(self.cont2) + " veces"
                print "No hay Página Recomendada"

            elif self.cont1 == 0 and self.cont2 == 0:
                print "\npalabra No Encontrada"
                print "No hay Página Recomendada\n"

            while respuesta != "no":
                respuesta = raw_input("Desea realizar otra busqueda si/no: \n")
                respuesta = respuesta.lower()

                try:
                    respuesta = float(respuesta)
                    respuesta = int(respuesta)
                    print "Error Desea realizar otra busqueda: \n"
                except(RuntimeError, NameError, ValueError):
                    respuesta = respuesta

                if respuesta == "si":
                    self.pagina1 = ""
                    self.pagina2 = ""
                    self.palabra = ""
                    time.sleep(1)
                    os.system("clear")

                    break

                elif respuesta == "no":
                    break

                else:
                    print"\n  Error debe ingresar una opción válida\n"
        raw_input("Presione Enter para continuar ...")
        os.system("clear")
        return

    def menu(self):
        self.oportunidad = 0
        while True:
            while (self.oportunidad != 1) or (self.oportunidad != 2):

                print"                    ***** Motor de Busqueda © ***** \n"
                print "1. Ingresar Busqueda"
                print "2. Salir"

                self.oportunidad = raw_input("Ingresa una opción: ")
                try:
                    self.oportunidad = int(self.oportunidad)
                    if self.oportunidad > 0 and self.oportunidad <= 2:
                        break
                    else:
                        print "Ingrese opción válida\n"
                        time.sleep(1)
                        os.system("clear")
                except(RuntimeError, TypeError, NameError, ValueError):
                    print "Ingrese opción válida\n"
                    time.sleep(1)
                    os.system("clear")

            if self.oportunidad == 1:
                inicio = _Motor()
                inicio.busqueda()

            if self.oportunidad == 2:
                print "Saliendo ..."
                time.sleep(2)
                os.system("clear")
                print"                            ***** Motor de Busqueda © ***** \n"
                print u"                      Third Generation Grupo: KAR-FER :\n"
                print u"                                 **************"
                print u"                                 Kevin Herrera"
                print u"                                 **************\n"
                print u"                          KAR_KO,INDUSTRIS Copright ®"
                time.sleep(1)
                sys.exit()
        self.oportunidad = 0
        return

START = _Motor()
START.menu()


