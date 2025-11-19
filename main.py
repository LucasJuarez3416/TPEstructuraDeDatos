from servidor_correo import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje

def main():
    # Crear servidores
    servidor1 = ServidorCorreo("Servidor1")
    servidor2 = ServidorCorreo("Servidor2")
    servidor3 = ServidorCorreo("Servidor3")

    # Conectar servidores (grafo)
    servidor1.conectar(servidor2)
    servidor2.conectar(servidor3)

    # Crear usuarios
    lucas = Usuario("Lucas", "lucas@mail.com", "1234")
    jorge = Usuario("Jorge", "jorge@mail.com", "abcd")

    # Asignar servidores a usuarios
    lucas.servidor = servidor3
    jorge.servidor = servidor1

    # Registrar usuarios en sus servidores
    servidor1.registrar_usuario(jorge)
    servidor3.registrar_usuario(lucas)

    # Crear subcarpetas para Lucas
    lucas.crear_subcarpeta("Bandeja de entrada", "Trabajo")
    lucas.crear_subcarpeta("Trabajo", "Proyectos")
    lucas.crear_subcarpeta("Bandeja de entrada", "Familia")

    # Crear mensajes
    mensaje1 = Mensaje(
        origen=jorge,
        destino=lucas,
        asunto="Nos vemos mañana",
        contenido="Recordá traer los documentos.",
        urgente=False
    )

    mensaje2 = Mensaje(
        origen=jorge,
        destino=lucas,
        asunto="Reunión urgente",
        contenido="Tenemos una reunión urgente.",
        urgente=True
    )

    # Enviar mensajes al servidor origen
    servidor1.enviar_mensaje(mensaje1) 
    servidor1.enviar_mensaje(mensaje2)

    # Procesar mensajes del servidor origen (urgentes primero)
    servidor1.procesar_mensajes()

    print("\nEstructura de carpetas:")
    lucas.mostrar_carpetas()

    print("\nMensajes en bandeja de entrada:")
    for msg in lucas.listar_inbox():
        print(msg.mostrar_resumen())

    print("\nBúsqueda de 'Reunión':")
    for msg in lucas.buscar_mensajes("Reunión"):
        print(msg.mostrar_resumen())


if __name__ == "__main__":
    main()
