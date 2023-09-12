class pilaAnimalesObjetos:
    def __init__(self):
        self.items = []
    def apilar(self, elemento):
        self.items.append(elemento)
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
    def esta_vacia(self):
        return len(self.items) == 0
# Crear una pila
pila_elementos = pilaAnimalesObjetos()
# Apilar elementos en la pila
pila_elementos.apilar("perro")
pila_elementos.apilar("gato")
pila_elementos.apilar("carro")
pila_elementos.apilar("víbora")
# Desapilar y mostrar elementos
print(pila_elementos.desapilar())
print(pila_elementos.desapilar())
print(pila_elementos.desapilar())
print(pila_elementos.desapilar())