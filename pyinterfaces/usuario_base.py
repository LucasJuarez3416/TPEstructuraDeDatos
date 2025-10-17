from abc import ABC, abstractmethod

class UsuarioBase(ABC):
    @abstractmethod
    def recibir_mensaje(self, mensaje):
        pass

    @abstractmethod
    def listar_inbox(self):
        pass
