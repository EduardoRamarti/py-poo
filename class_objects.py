#Definicion de la clase 
class Drink:
    #Constructor
    def __init__(self, name):
        self.__name = name #encapsulando el atributo (volviendolo privado con doble guion bajo)
    #Metodo 
    def getDatail(self):
        return f"la bebida es: {self.__name}" #solo podemos acceder por medio de este metodo 

#Instanciar un objeto
drink = Drink("agua")

class Product:
    def __init__(self, cost, price):
        self.cost = cost
        self.price = price
    def getGain(self):
        return self.price - self.cost


class Beer(Drink, Product):
    #atributo estatico
    Count = 0

    def __init__(self, name, brand, alcohol, cost, price):
        #super().__init__(name) #Llamando al constructor de la clase padre y pasarle el nombre. super hace referencia a la clase padre.
        Drink.__init__(self,name) #En lugar de usar super, tambien se puede utilizar el nombre directo de la clase padre
        Product.__init__(self,cost, price) #siempre que se usa el nombre de la clase padre, hay que usar self en los parametros
        self.brand = brand
        self.alcohol = alcohol
        Beer.Count += 1
    def getDatail(self):
        return super().getDatail() + " de la marca: " + self.brand + " con alcohol: " + str(self.alcohol)
    # El polimorfismo es como hacer una sobre escritura, es decir, es la capacidad de un metodo de responder diferente a cada situacion siendo el mismo
    # aqui en este metodo que es mismo que el metodo del padre, el padre se llama y se le concatenan otros strings 
    # siempre que haya el mismo metodo en clase padre e hijo, se llamada la clase hijo en el objeto instanciado de este
    
    @staticmethod #volviendo estatico este metodo con el decorador
    def getClassInfo(text=""): #tiene un parametro opcional 
        return "se ha creado " + str(Beer.Count) + " Objetos"

beer1 = Beer("Pale Ale", "Minerva", 4.5, 10, 20)
print(beer1.getDatail())#desde la clase hijo tambien se puede acceder a los metodos de la clase padre

beer2 = Beer("Stout", "Minerva", 6, 10, 22)
print(beer2.getDatail())

#llamando al atributo estatico
print(Beer.Count)#sera 2 ya que se han creado dos objetos 
print(Beer.getClassInfo())


