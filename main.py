def agregar_contacto(contactos):
    while True:
        nombre = input("Nómbre del contacto: ").strip()
        telefono = input("Número de Teléfono: ").strip()

        if not nombre or not telefono:
            print("Nombre y Teléfono no pueden estar vacíos. Por favor, inténtalo de nuevo.")
            continue

        for contacto in contactos:
            if contacto["telefono"] == telefono:
                print("Contacto ya existente")
                return
  
        contacto = {
        "nombre": nombre,
        "telefono": telefono
        }
        contactos.append(contacto)
        break

    print("Contácto guardado exitosamente.")

def eliminar_contacto(contactos):
    telefono = input("Número de Teléfono del contacto a eliminar: ").strip()

    for contacto in contactos:
        if contacto["telefono"] == telefono:
            contactos.remove(contacto)
            print("Contacto eliminado exitosamente.")
            return

    print("Contacto no encontrado.")

def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos para mostrar.")
        return

    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']} // Teléfono: {contacto['telefono']}")

def editar_contacto(contactos):
    if not contactos:
        print("No hay contactos para editar.")
        return
    
    telefono = input("Número de Teléfono del contacto a editar: ").strip()

    if not telefono:
        print("El número de teléfono no puede estar vacío. Por favor, inténtalo de nuevo.")
        return

    for contacto in contactos:
        if contacto["telefono"] == telefono:
            nuevo_nombre = input("Nuevo nombre del contacto: ").strip()
            nuevo_telefono = input("Nuevo número de teléfono: ").strip()

            if not nuevo_nombre or not nuevo_telefono:
                print("Nombre y Teléfono no pueden estar vacíos. Por favor, inténtalo de nuevo.")
                return
            
            for c in contactos:
                if c["telefono"] == nuevo_telefono and c != contacto:
                    print("El número de teléfono ya está asociado a otro contacto.")
                    return

            contacto["nombre"] = nuevo_nombre
            contacto["telefono"] = nuevo_telefono
            print("Contacto editado exitosamente.")
            return

    print("Contacto no encontrado.")

def menu():
    print("--------------------------------------------")
    print("          Agenda De Contactos AG")
    print("--------------------------------------------")
    print("1. AGREGAR CONTACTO")
    print("2. ELIMINAR CONTACTO")
    print("3. MOSTRAR CONTACTOS")
    print("4. EDITAR CONTACTO")
    print("5. SALIR")

def main():
    lista_contactos = []
    while True:
        menu()
        try:
            opcion = int(input("Elige una opción: "))

        except ValueError:
            print("Entrada inválida. Debes ingresar un número")
            continue 

        if opcion == 1:
            print("\n---- AGREGAR CONTACTO ----")
            agregar_contacto(lista_contactos)

        elif opcion == 2:
            print("\n---- ELIMINAR CONTACTO ----")
            eliminar_contacto(lista_contactos)

        elif opcion == 3:
            print("\n---- MOSTRAR CONTACTOS ----")
            mostrar_contactos(lista_contactos)

        elif opcion == 4:
            print("\n---- EDITAR CONTACTO ----")
            editar_contacto(lista_contactos)

        elif opcion == 5:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")  

if __name__ == "__main__":
    main()