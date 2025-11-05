class Mensaje:
    def __init__(self, origen, destino, contenido, urgente=False):
        self.origen = origen
        self.destino = destino
        self.contenido = contenido
        self.urgente = urgente

    def __repr__(self):
        prioridad = "URGENTE" if self.urgente else "Normal"
        return f"<Mensaje de {self.origen.nombre} a {self.destino.nombre} ({prioridad})>"
