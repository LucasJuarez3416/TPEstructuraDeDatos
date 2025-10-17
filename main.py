from TPEstructuraDeDatos.servidor_correo import ServidorCorreo
from TPEstructuraDeDatos.usuario import Usuario

def main():
    servidor = ServidorCorreo()
    lucas = Usuario("Lucas", "lucas@mail.com", "1234")
    servidor.registrar_usuario(lucas)

    lucas.crear_subcarpeta("Bandeja de entrada", "Trabajo")
    lucas.crear_subcarpeta("Trabajo", "Proyectos")
    lucas.crear_subcarpeta("Bandeja de entrada", "Familia")

    servidor.enviar_mensaje("jorge@mail.com", "lucas@mail.com", "Reunión", "Nos vemos mañana")
    servidor.enviar_mensaje("pablo@mail.com", "lucas@mail.com", "Fotos", "Te paso las fotos del finde")

    print("\n Estructura de carpetas:")
    lucas.mostrar_carpetas()

    print("\n Mensajes en bandeja de entrada:")
    for msg in lucas.listar_inbox():
        print(msg)

    print("\n Búsqueda de 'Reunión':")
    for msg in lucas.buscar_mensajes("Reunión"):
        print(msg.mostrar_resumen())

if __name__ == "__main__":
    main()
