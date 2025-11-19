from TPEstructuraDeDatos.pyinterfaces.carpeta_base import CarpetaBase

class Carpeta(CarpetaBase):
    def __init__(self, nombre, carpeta_padre=None):
        self.__nombre = nombre
        self.__mensajes = []
        self.__subcarpetas = []
        self.__carpeta_padre = carpeta_padre

    @property
    def nombre(self):
        return self.__nombre

    def agregar_mensaje(self, mensaje):
        self.__mensajes.append(mensaje)

    def listar_mensajes(self):
        # devuelve objetos Mensaje, no strings
        return self.__mensajes

    def agregar_subcarpeta(self, nombre_subcarpeta):
        subcarpeta = Carpeta(nombre_subcarpeta, carpeta_padre=self)
        self.__subcarpetas.append(subcarpeta)
        return subcarpeta

    def obtener_subcarpeta(self, nombre):
        if self.__nombre == nombre:
            return self
        for sub in self.__subcarpetas:
            resultado = sub.obtener_subcarpeta(nombre)
            if resultado:
                return resultado
        return None

    def mover_mensaje(self, mensaje, carpeta_destino):
        if mensaje in self.__mensajes:
            self.__mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)

    def buscar_mensajes_recursivo(self, texto_busqueda):
        resultados = []
        for msg in self.__mensajes:
            if texto_busqueda.lower() in msg.mostrar_resumen().lower():
                resultados.append(msg)

        for subcarpeta in self.__subcarpetas:
            resultados.extend(subcarpeta.buscar_mensajes_recursivo(texto_busqueda))

        return resultados

    def mostrar_estructura(self, nivel=0):
        print("  " * nivel + f"- {self.__nombre}")
        for sub in self.__subcarpetas:
            sub.mostrar_estructura(nivel + 1)
