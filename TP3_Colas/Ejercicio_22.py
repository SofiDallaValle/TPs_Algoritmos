"""22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
F) por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
b. mostrar los nombre de los superhéroes femeninos;
c. mostrar los nombres de los personajes masculinos;
d. determinar el nombre del superhéroe del personaje Scott Lang;
e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
con la letra S;
f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
de superhéroes."""

class Queue:
    def __init__(self):
        self._elements= []

    def arrive(self,value):
        self._elements.append(value)
    
    def attention(self):
        return (
            if self._elements:
                self._elements.pop(0)
            else None)
    
    def size(self) -> int:
        return len(self._elements)
    
    def on_front(self):
        return (
            if self._elements:
                self._elements[0] 
            else None)
    
    def move_to_end(self):
        if self._elements:
            value =self.attention()
            self.arrive(value)
            return value    
        
    def show(self):
        for i in range(len(self._elements)):
            print(self.move_to_end())

    #a. Función que determina el nombre del personaje de la superhéroe Capitana Marvel.
    def personaje_capitana_marvel(self):
        aux = Queue()
        encontrado = False

        while self.size() > 0:
            personaje = self.attention()
            nombre, heroe, genero = personaje
            if heroe.lower() == "capitana marvel":
                print(f"El personaje de Capitana Marvel es: {nombre}")
                encontrado = True
            aux.arrive(personaje)

        while aux.size() > 0:
            self.arrive(aux.attention())
        if not encontrado:
            print("Capitana Marvel no se encuentra en la cola.")

    #b. Función que muestra los nombre de los superhéroes femeninos.
    def superheroes_femeninos(self):
        aux = Queue()
        encontrados = False
        print("Superhéroes femeninos:")

        while self.size() > 0:
            personaje = self.attention()
            nombre, heroe, genero = personaje
            if genero.upper() == "F" :
                print(heroe)
                encontrados = True
            aux.arrive(personaje)

        while aux.size() > 0:
            self.arrive(aux.attention())
        
        if not encontrados:
            print("No hay superhéroes femeninos en la cola.")

    #c. Función que muestra los nombres de los personajes masculinos.
    def personajes_masculinos(self):
        aux = Queue()
        encontrados = False
        print("Personajes masculinos: ")

        while self.size() > 0:
            personaje = self.attention()
            nombre, heroe, genero = personaje
            if genero.upper() =="M":
                print(nombre)
                encontrados = True
            aux.arrive(personaje)

        while aux.size() > 0:
            self.arrive(aux.attention())

        if not encontrados:
            print("No hay personajes masculinos en la cola.")

    #d. Función que determina el nombre del superhéroe del personaje Scott Lang.
    def heroe_scott_lang(self):
        aux = Queue()
        encontrado = False

        while self.size() > 0:
            personaje = self.attention()
            nombre, heroe, genero = personaje
            if nombre.lower() == "scott lang":
                print(f"El superhéroe de Scott Lang es: {heroe}")
                encontrado = True
            aux.arrive(personaje)
        
        while aux.size() > 0:
            self.arrive(aux.attention())
        if not encontrado:
            print("Scott Lang no se encuentra en la cola.")


    #e. Función que muestra todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S.
    def datos_nombres_s(self):
        aux = Queue()
        encontrados = False
        print("Personajes o superhéroes cuyos nombres comienzan con S: ")

        while self.size() > 0: 
            personaje = self.attention()
            nombre, heroe, genero = personaje
            if nombre.upper().startswith("S") or heroe.upper().startswith("S"):
                print(f"Nombre: {nombre}, Superhéroe: {heroe}, Género: {genero}")
                encontrados = True
            aux.arrive (personaje)

        while aux.size() > 0:
            self.arrive(aux.attention())
        if not encontrados: 
            print("No hay personajes o superhéroes cuyos nombres comienzan con la letra S en la cola.")

    #f. Función que determina si el personaje Carol Danvers se encuentra en la cola e indica su nombre de superhéroes.
    def carol_danvers(self):
        aux = Queue()
        encontrado = False

        while self.size() > 0:
            personaje = self.attention()
            nombre, heroe, genero = personaje
            if nombre.lower() == "carol danvers":
                print(f"Carol Danvers se encuentra en la cola y su nombre de superhéroe es: {heroe}")
                encontrado = True
            aux.arrive(personaje)

        while aux.size() > 0:
            self.arrive(aux.attention())
        if not encontrado:
            print("Carol Danvers no se encuentra en la cola.")

    #Ejemplo de uso:

queue = Queue()
queue.arrive(("Tony Stark", "Iron Man", "M"))
queue.arrive(("Steve Rogers", "Capitán América", "M"))
queue.arrive(("Natasha Romanoff", "Black Widow", "F"))
queue.arrive(("Carol Danvers", "Capitana Marvel", "F"))
queue.arrive(("Scott Lang", "Ant-Man", "M"))
queue.personaje_capitana_marvel()
queue.superheroes_femeninos()
queue.personajes_masculinos()
queue.heroe_scott_lang()
queue.datos_nombres_s()
queue.carol_danvers()
