from TPEstructuraDeDatos.servidor_correo import ServidorCorreo
from TPEstructuraDeDatos.usuario import Usuario
from TPEstructuraDeDatos.mensaje import Mensaje

def main():
    # Crear servidores (grafo)
    servidor1 = ServidorCorreo("Servidor1")
    servidor2 = ServidorCorreo("Servidor2")
    servidor3 = ServidorCorreo("Servidor3")

    # Conectar servidores
    servidor1.conectar(servidor2)
    servidor2.conectar(servidor3)

    # Crear usuarios y asignarlos a servidores
    lucas = Usuario("Lucas", "lucas@mail.com", "1234")
    jorge = Usuario("Jorge", "jorge@mail.com", "abcd")

    # Asignar servidores (esto depende de tu implementación de Usuario)
    lucas.servidor = servidor3
    jorge.servidor = servidor1

    # Registrar usuarios en sus servidores
    if hasattr(servidor1, "registrar_usuario"):
        servidor1.registrar_usuario(jorge)
    if hasattr(servidor3, "registrar_usuario"):
        servidor3.registrar_usuario(lucas)

    # Crear subcarpetas para Lucas
    lucas.crear_subcarpeta("Bandeja de entrada", "Trabajo")
    lucas.crear_subcarpeta("Trabajo", "Proyectos")
    lucas.crear_subcarpeta("Bandeja de entrada", "Familia")

    # Enviar mensajes normales y urgentes
    mensaje1 = Mensaje(jorge, lucas, "Nos vemos mañana", urgente=False)
    mensaje2 = Mensaje(jorge, lucas, "¡Mensaje urgente de reunión!", urgente=True)

    # Enviar los mensajes al servidor origen
    servidor1.recibir_mensaje(mensaje1)
    servidor1.recibir_mensaje(mensaje2)

    # Procesar mensajes (el urgente se entrega primero)
    servidor1.procesar_mensajes()

    print("\n📂 Estructura de carpetas:")
    lucas.mostrar_carpetas()

    print("\n📬 Mensajes en bandeja de entrada:")
    for msg in lucas.listar_inbox():
        print(msg)

    print("\n🔎 Búsqueda de 'Reunión':")
    for msg in lucas.buscar_mensajes("Reunión"):
        print(msg.mostrar_resumen())

if __name__ == "__main__":
    main()
