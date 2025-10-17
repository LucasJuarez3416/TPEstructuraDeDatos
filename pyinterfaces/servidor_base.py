from abc import ABC, abstractmethod

class ServidorBase(ABC):
    @abstractmethod
    def registrar_usuario(self, usuario):
        pass

    @abstractmethod
    def enviar_mensaje(self, remitente, destinatario, asunto, cuerpo):
        pass
