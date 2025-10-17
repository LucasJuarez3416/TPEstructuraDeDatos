from abc import ABC, abstractmethod

class CarpetaBase(ABC):
    @abstractmethod
    def agregar_mensaje(self, mensaje):
        pass

    @abstractmethod
    def listar_mensajes(self):
        pass
