class Paquete:
    def __init__(self, id, datos):
        self.id = id
        self.datos = datos
        self.prev = None
        self.next = None

class ColaPaquetes:
    def __init__(self):
        self.head = None
        self.tail = None
        self.actual = None
        self.contador = 1  # IDs automáticos

    def agregar_paquete(self, datos):
        nuevo = Paquete(self.contador, datos)
        self.contador += 1

        if not self.head:  # lista vacía
            self.head = self.tail = self.actual = nuevo
        else:
            self.tail.next = nuevo
            nuevo.prev = self.tail
            self.tail = nuevo
        print(f" Paquete agregado: ID={nuevo.id}, Datos='{nuevo.datos}'")

    def eliminar_paquete_actual(self):
        if not self.actual:
            print(" No hay paquetes para eliminar.")
            return
        print(f" Eliminando paquete ID={self.actual.id}, Datos='{self.actual.datos}'")

        if self.actual.prev:
            self.actual.prev.next = self.actual.next
        else:
            self.head = self.actual.next

        if self.actual.next:
            self.actual.next.prev = self.actual.prev
            self.actual = self.actual.next
        else:
            self.tail = self.actual.prev
            self.actual = self.tail

    def adelantar(self):
        if self.actual and self.actual.next:
            self.actual = self.actual.next
            print(f" Adelantado a paquete ID={self.actual.id}")
        else:
            print(" No hay más paquetes adelante.")

    def retroceder(self):
        if self.actual and self.actual.prev:
            self.actual = self.actual.prev
            print(f" Retrocedido a paquete ID={self.actual.id}")
        else:
            print(" No hay más paquetes atrás.")

    def procesar_actual(self):
        if not self.actual:
            print(" No hay paquetes para procesar.")
            return
        print(f" Procesando paquete ID={self.actual.id}, Datos='{self.actual.datos}'")
        self.eliminar_paquete_actual()

    def mostrar_paquetes(self):
        if not self.head:
            print("📭 No hay paquetes en la cola.")
            return
        actual = self.head
        print(" Cola de Paquetes:")
        while actual:
            marcador = " <= [ACTUAL]" if actual == self.actual else ""
            print(f"   ID={actual.id}, Datos='{actual.datos}'{marcador}")
            actual = actual.next

    # 🔹 NUEVA FUNCIÓN 1: Buscar paquete por ID
    def buscar_paquete(self, id_buscar):
        actual = self.head
        while actual:
            if actual.id == id_buscar:
                print(f" Paquete encontrado: ID={actual.id}, Datos='{actual.datos}'")
                return
            actual = actual.next
        print(f" Paquete con ID={id_buscar} no encontrado.")

    # 🔹 NUEVA FUNCIÓN 2: Vaciar toda la cola
    def vaciar_cola(self):
        self.head = None
        self.tail = None
        self.actual = None
        print(" Cola de paquetes vaciada completamente.")

# ----------------- MENÚ -----------------
def menu():
    cola = ColaPaquetes()
    while True:
        print("\n==== MENÚ SIMULACIÓN DE RED ====")
        print("1. Agregar paquete")
        print("2. Eliminar paquete actual")
        print("3. Adelantar")
        print("4. Retroceder")
        print("5. Procesar paquete actual")
        print("6. Mostrar cola de paquetes")
        print("7. Buscar paquete por ID")
        print("8. Vaciar cola")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = input("Ingrese datos del paquete: ")
            cola.agregar_paquete(datos)
        elif opcion == "2":
            cola.eliminar_paquete_actual()
        elif opcion == "3":
            cola.adelantar()
        elif opcion == "4":
            cola.retroceder()
        elif opcion == "5":
            cola.procesar_actual()
        elif opcion == "6":
            cola.mostrar_paquetes()
        elif opcion == "7":
            try:
                id_buscar = int(input("Ingrese el ID del paquete a buscar: "))
                cola.buscar_paquete(id_buscar)
            except ValueError:
                print(" Debe ingresar un número válido.")
        elif opcion == "8":
            cola.vaciar_cola()
        elif opcion == "9":
            print(" Saliendo de la simulación...")
            break
        else:
            print(" Opción inválida, intente de nuevo.")

# Ejecutar menú
if __name__ == "__main__":
    menu()
