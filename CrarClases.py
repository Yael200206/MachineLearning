class Vehiculo:
    def __init__(self, marca, modelo, año):
        print("se constryo el carro")
        self.marca = marca     
        self.modelo = modelo    
        self.año = año
               



class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre    
        self.especie = especie  
        self.edad = edad        

auto1 = Vehiculo("Toyota", "Corolla", 2024)
auto2 = Vehiculo("Tesla", "Model 3", 2023)

mascota1 = Mascota("Leo", "Perro", 3)
mascota2 = Mascota("Manuel", "Gato", 5)

print(auto1 , auto2.año)

print()

print(mascota1  , mascota2.edad)
