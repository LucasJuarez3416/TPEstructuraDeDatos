from datetime import datetime
from TPEstructuraDeDatos.pyinterfaces.mensaje_base import MensajeBase

class Mensaje(MensajeBase):
    def __init__(self, remitente, destinatario, asunto, cuerpo):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__cuerpo = cuerpo
        self.__fecha = datetime.now()

    def mostrar_resumen(self):
        return (
            f"[{self.__fecha.strftime('%d/%m/%Y %H:%M')}] "
            f"De: {self.__remitente} | Asunto: {self.__asunto} | Cuerpo: {self.__cuerpo}"
        )
