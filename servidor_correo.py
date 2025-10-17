from TPEstructuraDeDatos.pyinterfaces.servidor_base import ServidorBase
from TPEstructuraDeDatos.mensaje import Mensaje

class ServidorCorreo(ServidorBase):
    def __init__(self):
        self.__usuarios = {}

    def registrar_usuario(self, usuario):
        self.__usuarios[usuario.email] = usuario

    def enviar_mensaje(self, remitente, destinatario_email, asunto, cuerpo):
        if destinatario_email in self.__usuarios:
            mensaje = Mensaje(remitente, destinatario_email, asunto, cuerpo)
            self.__usuarios[destinatario_email].recibir_mensaje(mensaje)
            print(f"Mensaje enviado a {destinatario_email} por {remitente}")
        else:
            print(f"Error: {destinatario_email} no está registrado en el servidor.")

    def buscar_usuario(self, email):
        return self.__usuarios.get(email, None)
