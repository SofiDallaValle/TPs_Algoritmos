"""5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
se (MCU), desarrollar un algoritmo que contemple lo siguiente:

a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
leano que indica si es un héroe o un villano, True y False respectivamente;
b. listar los villanos ordenados alfabéticamente;
c. mostrar todos los superhéroes que empiezan con C;
d. determinar cuántos superhéroes hay el árbol;
e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
f. listar los superhéroes ordenados de manera descendente;
g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:
I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol."""

from collections import deque

class Nodo:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe  # True = héroe | False = villano
        self.izq = None
        self.der = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        self.raiz = self._insertar(self.raiz, nombre, es_heroe)

    def _insertar(self, nodo, nombre, es_heroe):
        if nodo is None:
            return Nodo(nombre, es_heroe)

        if nombre < nodo.nombre:
            nodo.izq = self._insertar(nodo.izq, nombre, es_heroe)
        else:
            nodo.der = self._insertar(nodo.der, nombre, es_heroe)

        return nodo

    def buscar(self, nodo, nombre):
        if nodo is None:
            return None
        if nodo.nombre == nombre:
            return nodo
        elif nombre < nodo.nombre:
            return self.buscar(nodo.izq, nombre)
        else:
            return self.buscar(nodo.der, nombre)

    #a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
    #leano que indica si es un héroe o un villano, True y False respectivamente;
    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.nombre, "-", "Héroe" if nodo.es_heroe else "Villano")
            self.inorden(nodo.der)

    #b. listar los villanos ordenados alfabéticamente;
    def listar_villanos(self, nodo):
        if nodo:
            self.listar_villanos(nodo.izq)
            if not nodo.es_heroe:
                print(nodo.nombre)
            self.listar_villanos(nodo.der)

    #c. mostrar todos los superhéroes que empiezan con C;
    def heroes_con_c(self, nodo):
        if nodo:
            self.heroes_con_c(nodo.izq)
            if nodo.es_heroe and nodo.nombre.startswith("C"):
                print(nodo.nombre)
            self.heroes_con_c(nodo.der)

    #d. determinar cuántos superhéroes hay el árbol;
    def contar_heroes(self, nodo):
        if nodo is None:
            return 0

        contador = 1 if nodo.es_heroe else 0
        contador += self.contar_heroes(nodo.izq)
        contador += self.contar_heroes(nodo.der)

        return contador

    #e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
    #encontrarlo en el árbol y modificar su nombre;
    def busqueda_proximidad(self, nodo, texto):
        if nodo:
            self.busqueda_proximidad(nodo.izq, texto)
            if texto.lower() in nodo.nombre.lower():
                print(nodo.nombre)
            self.busqueda_proximidad(nodo.der, texto)

    def modificar_nombre(self, nombre_actual, nuevo_nombre):
        nodo = self.buscar(self.raiz, nombre_actual)
        if nodo:
            es_heroe = nodo.es_heroe
            self.eliminar(nombre_actual)
            self.insertar(nuevo_nombre, es_heroe)

    #f. listar los superhéroes ordenados de manera descendente;
    def heroes_descendente(self, nodo):
        if nodo:
            self.heroes_descendente(nodo.der)
            if nodo.es_heroe:
                print(nodo.nombre)
            self.heroes_descendente(nodo.izq)

    def eliminar(self, nombre):
        self.raiz = self._eliminar(self.raiz, nombre)

    def _eliminar(self, nodo, nombre):
        if nodo is None:
            return nodo

        if nombre < nodo.nombre:
            nodo.izq = self._eliminar(nodo.izq, nombre)

        elif nombre > nodo.nombre:
            nodo.der = self._eliminar(nodo.der, nombre)

        else:
            if nodo.izq is None and nodo.der is None:
                return None

            if nodo.izq is None:
                return nodo.der
            if nodo.der is None:
                return nodo.izq

            sucesor = self._minimo(nodo.der)
            nodo.nombre = sucesor.nombre
            nodo.es_heroe = sucesor.es_heroe
            nodo.der = self._eliminar(nodo.der, sucesor.nombre)

        return nodo

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    #g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
    #los villanos, luego resolver las siguiente tareas:
    def generar_bosque(self):
        arbol_heroes = Arbol()
        arbol_villanos = Arbol()

        def recorrer(nodo):
            if nodo:
                if nodo.es_heroe:
                    arbol_heroes.insertar(nodo.nombre, True)
                else:
                    arbol_villanos.insertar(nodo.nombre, False)

                recorrer(nodo.izq)
                recorrer(nodo.der)

        recorrer(self.raiz)
        return arbol_heroes, arbol_villanos

    # g I. determinar cuántos nodos tiene cada árbol;
    def contar_nodos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar_nodos(nodo.izq) + self.contar_nodos(nodo.der)

    # g II. realizar un barrido ordenado alfabéticamente de cada árbol.
    def barrido_alfabetico(self, nodo):
        if nodo:
            self.barrido_alfabetico(nodo.izq)
            print(nodo.nombre)
            self.barrido_alfabetico(nodo.der)

    def por_nivel(self):
        if not self.raiz:
            return

        cola = deque([self.raiz])

        while cola:
            nodo = cola.popleft()
            print(nodo.nombre)
            if nodo.izq:
                cola.append(nodo.izq)
            if nodo.der:
                cola.append(nodo.der)

 #Ejemplo de uso:
arbol = Arbol()

datos = [
    ("Iron Man", True),
    ("Thanos", False),
    ("Captain America", True),
    ("Loki", False),
    ("Doctor Strang", True),  # mal cargado
    ("Black Widow", True),
    ("Ultron", False),
    ("Hulk", True),
    ("Green Goblin", False),
    ("Scarlet Witch", True)
]

for nombre, es_heroe in datos:
    arbol.insertar(nombre, es_heroe)

print("\nVillanos:")
arbol.listar_villanos(arbol.raiz)

print("\nHéroes con C:")
arbol.heroes_con_c(arbol.raiz)

print("\nCantidad de héroes:")
print(arbol.contar_heroes(arbol.raiz))

print("\nBúsqueda por proximidad 'Strang':")
arbol.busqueda_proximidad(arbol.raiz, "Strang")

print("\nCorrigiendo nombre...")
arbol.modificar_nombre("Doctor Strang", "Doctor Strange")

print("\nHéroes descendente:")
arbol.heroes_descendente(arbol.raiz)

print("\nGenerando bosque...")
heroes, villanos = arbol.generar_bosque()

print("\nCantidad nodos árbol héroes:")
print(heroes.contar_nodos(heroes.raiz))

print("\nCantidad nodos árbol villanos:")
print(villanos.contar_nodos(villanos.raiz))

print("\nBarrido héroes:")
heroes.barrido_alfabetico(heroes.raiz)

print("\nBarrido villanos:")
villanos.barrido_alfabetico(villanos.raiz)