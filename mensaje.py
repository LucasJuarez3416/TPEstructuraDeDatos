class Mensaje:
    def __init__(self, origen, destino, asunto, contenido, urgente=False):
        self.origen = origen
        self.destino = destino
        self.asunto = asunto
        self.contenido = contenido
        self.urgente = urgente

    def mostrar_resumen(self):
        prioridad = "URGENTE" if self.urgente else "Normal"
        return f"[{prioridad}] {self.asunto} - de {self.origen.nombre} para {self.destino.nombre}"

    def __repr__(self):
        return self.mostrar_resumen()
