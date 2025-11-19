from pyinterfaces.usuario_base import UsuarioBase
from carpeta import Carpeta

class Usuario(UsuarioBase):
    def __init__(self, nombre, email, password):
        self.__nombre = nombre
        self.__email = email
        self.__password = password
        self.__raiz = Carpeta("Bandeja de entrada")
        self.servidor = None   # necesario para servidor_correo

    @property
    def email(self):
        return self.__email

    @property
    def nombre(self):
        return self.__nombre

    def recibir_mensaje(self, mensaje):
        self.__raiz.agregar_mensaje(mensaje)

    def listar_inbox(self):
        return self.__raiz.listar_mensajes()

    def crear_subcarpeta(self, nombre_padre, nombre_nueva):
        carpeta_padre = self.__raiz.obtener_subcarpeta(nombre_padre)
        if carpeta_padre:
            carpeta_padre.agregar_subcarpeta(nombre_nueva)
        else:
            print(f"No se encontró la carpeta '{nombre_padre}'")

    def mover_mensaje(self, asunto, carpeta_destino):
        resultados = self.__raiz.buscar_mensajes_recursivo(asunto)

        if not resultados:
            print("No se encontró ningún mensaje con ese asunto.")
            return

        mensaje = resultados[0]
        origen = self.__raiz                  # origen correcto
        destino = self.__raiz.obtener_subcarpeta(carpeta_destino)

        if destino:
            origen.mover_mensaje(mensaje, destino)
            print(f"Mensaje movido a {carpeta_destino}")
        else:
            print("Carpeta destino no encontrada.")

    def buscar_mensajes(self, texto_busqueda):
        return self.__raiz.buscar_mensajes_recursivo(texto_busqueda)

    def mostrar_carpetas(self):
        self.__raiz.mostrar_estructura()
