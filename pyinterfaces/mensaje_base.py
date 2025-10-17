from abc import ABC, abstractmethod

class MensajeBase(ABC):
    @abstractmethod
    def mostrar_resumen(self):
        pass
