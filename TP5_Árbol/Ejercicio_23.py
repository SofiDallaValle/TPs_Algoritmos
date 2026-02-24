"""23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
a. listado inorden de las criaturas y quienes la derrotaron;
b. se debe permitir cargar una breve descripción sobre cada criatura;
c. mostrar toda la información de la criatura Talos;
d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e. listar las criaturas derrotadas por Heracles;
f. listar las criaturas que no han sido derrotadas;
g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
i. se debe permitir búsquedas por coincidencia;
j. eliminar al Basilisco y a las Sirenas;
k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
l. modifique el nombre de la criatura Ladón por Dragón Ladón;
m. realizar un listado por nivel del árbol;
n. muestre las criaturas capturadas por Heracles."""

from collections import deque

class Nodo:
    def __init__(self, criatura, derrotado_por):
        self.criatura = criatura
        self.derrotado_por = derrotado_por
        self.descripcion = ""
        self.capturada = None
        self.izq = None
        self.der = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, criatura, derrotado_por):
        self.raiz = self._insertar(self.raiz, criatura, derrotado_por)

    def _insertar(self, nodo, criatura, derrotado_por):
        if nodo is None:
            return Nodo(criatura, derrotado_por)

        if criatura < nodo.criatura:
            nodo.izq = self._insertar(nodo.izq, criatura, derrotado_por)
        else:
            nodo.der = self._insertar(nodo.der, criatura, derrotado_por)

        return nodo

    def buscar(self, nodo, nombre):
        if nodo is None:
            return None
        if nodo.criatura == nombre:
            return nodo
        elif nombre < nodo.criatura:
            return self.buscar(nodo.izq, nombre)
        else:
            return self.buscar(nodo.der, nombre)

    def eliminar(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre)

    def _eliminar(self, nodo, nombre):
        if nodo is None:
            return nodo

        if nombre < nodo.criatura:
            nodo.izq = self._eliminar(nodo.izq, nombre)

        elif nombre > nodo.criatura:
            nodo.der = self._eliminar(nodo.der, nombre)

        else:
            if nodo.izq is None and nodo.der is None:
                return None

            if nodo.izq is None:
                return nodo.der
            if nodo.der is None:
                return nodo.izq

            sucesor = self._minimo(nodo.der)
            nodo.criatura = sucesor.criatura
            nodo.derrotado_por = sucesor.derrotado_por
            nodo.der = self._eliminar(nodo.der, sucesor.criatura)

        return nodo

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    #a. listado inorden de las criaturas y quienes la derrotaron;
    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.criatura, "-", nodo.derrotado_por)
            self.inorden(nodo.der)

    #b. se debe permitir cargar una breve descripción sobre cada criatura;
    def agregar_descripcion(self, nombre, descripcion):
        nodo = self.buscar(self.raiz, nombre)
        if nodo:
            nodo.descripcion = descripcion

    #c. mostrar toda la información de la criatura Talos;
    def mostrar_info(self, nombre):
        nodo = self.buscar(self.raiz, nombre)
        if nodo:
            print("Criatura:", nodo.criatura)
            print("Derrotado por:", nodo.derrotado_por)
            print("Descripción:", nodo.descripcion)
            print("Capturada por:", nodo.capturada)
        else:
            print("No encontrada")

    #d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
    def contar_derrotas(self, nodo, conteo):
        if nodo:
            if nodo.derrotado_por != "-":
                conteo[nodo.derrotado_por] = conteo.get(nodo.derrotado_por, 0) + 1
            self.contar_derrotas(nodo.izq, conteo)
            self.contar_derrotas(nodo.der, conteo)

    def top_3(self):
        conteo = {}
        self.contar_derrotas(self.raiz, conteo)
        ordenado = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
        print(ordenado[:3])

    #e. listar las criaturas derrotadas por Heracles;
    def derrotadas_por(self, nodo, nombre):
        if nodo:
            self.derrotadas_por(nodo.izq, nombre)
            if nodo.derrotado_por == nombre:
                print(nodo.criatura)
            self.derrotadas_por(nodo.der, nombre)

    #f. listar las criaturas que no han sido derrotadas;
    def no_derrotadas(self, nodo):
        if nodo:
            self.no_derrotadas(nodo.izq)
            if nodo.derrotado_por == "-":
                print(nodo.criatura)
            self.no_derrotadas(nodo.der)

    #h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
    #Erimanto indicando que Heracles las atrapó;
    def marcar_capturada(self, nombre):
        nodo = self.buscar(self.raiz, nombre)
        if nodo:
            nodo.capturada = "Heracles"

    #i. se debe permitir búsquedas por coincidencia;
    def busqueda_parcial(self, nodo, texto):
        if nodo:
            self.busqueda_parcial(nodo.izq, texto)
            if texto.lower() in nodo.criatura.lower():
                print(nodo.criatura)
            self.busqueda_parcial(nodo.der, texto)

    #k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
    #derroto a varias;
    def modificar_aves(self):
        nodo = self.buscar(self.raiz, "Aves del Estínfalo")
        if nodo:
            nodo.derrotado_por = "Heracles (derrotó varias)"

    #l. modifique el nombre de la criatura Ladón por Dragón Ladón;
    def modificar_ladon(self):
        nodo = self.buscar(self.raiz, "Ladón")
        if nodo:
            derrotado = nodo.derrotado_por
            self.eliminar("Ladón")
            self.insertar("Dragón Ladón", derrotado)

    #m. realizar un listado por nivel del árbol;
    def por_nivel(self):
        if not self.raiz:
            return

        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            print(nodo.criatura)

            if nodo.izq:
                cola.append(nodo.izq)
            if nodo.der:
                cola.append(nodo.der)

    #n. muestre las criaturas capturadas por Heracles.
    def capturadas_por(self, nodo, nombre):
        if nodo:
            self.capturadas_por(nodo.izq, nombre)
            if nodo.capturada == nombre:
                print(nodo.criatura)
            self.capturadas_por(nodo.der, nombre)



arbol = Arbol()

datos = [
    ("Ceto", "-"), ("Tifón", "Zeus"), ("Equidna", "Argos Panoptes"),
    ("Dino", "-"), ("Pefredo", "-"), ("Enio", "-"), ("Escila", "-"),
    ("Caribdis", "-"), ("Euríale", "-"), ("Esteno", "-"),
    ("Medusa", "Perseo"), ("Ladón", "Heracles"),
    ("Águila del Cáucaso", "-"), ("Quimera", "Belerofonte"),
    ("Hidra de Lerna", "Heracles"), ("León de Nemea", "Heracles"),
    ("Esfinge", "Edipo"), ("Dragón de la Cólquida", "-"),
    ("Cerbero", "-"), ("Cerda de Cromión", "Teseo"),
    ("Ortro", "Heracles"), ("Toro de Creta", "Teseo"),
    ("Jabalí de Calidón", "Atalanta"), ("Carcinos", "-"),
    ("Gerión", "Heracles"), ("Cloto", "-"), ("Láquesis", "-"),
    ("Átropos", "-"), ("Minotauro de Creta", "Teseo"),
    ("Harpías", "-"), ("Argos Panoptes", "Hermes"),
    ("Aves del Estínfalo", "-"), ("Talos", "Medea"),
    ("Sirenas", "-"), ("Pitón", "Apolo"),
    ("Cierva de Cerinea", "-"), ("Basilisco", "-"),
    ("Jabalí de Erimanto", "-")
]

for criatura, derrotado in datos:
    arbol.insertar(criatura, derrotado)

# modificaciones
arbol.marcar_capturada("Cerbero")
arbol.marcar_capturada("Toro de Creta")
arbol.marcar_capturada("Cierva de Cerinea")
arbol.marcar_capturada("Jabalí de Erimanto")

arbol.eliminar("Basilisco")
arbol.eliminar("Sirenas")

arbol.modificar_aves()
arbol.modificar_ladon()

#Ejemplo de uso:

print("\nINORDEN:")
arbol.inorden(arbol.raiz)

print("\nINFO TALOS:")
arbol.mostrar_info("Talos")

print("\nTOP 3 DERROTADORES:")
arbol.top_3()

print("\nDERROTADAS POR HERACLES:")
arbol.derrotadas_por(arbol.raiz, "Heracles")

print("\nNO DERROTADAS:")
arbol.no_derrotadas(arbol.raiz)

print("\nPOR NIVEL:")
arbol.por_nivel()

print("\nCAPTURADAS POR HERACLES:")
arbol.capturadas_por(arbol.raiz, "Heracles")