import heapq
from collections import deque

class ServidorCorreo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []        # Servidores conectados (grafo)
        self.mensajes = []          # Cola normal de mensajes
        self.cola_prioridad = []    # Cola de prioridad (urgentes)
        self.usuarios = []          # Lista de usuarios registrados en este servidor

    def registrar_usuario(self, usuario):
        """Registra un usuario en este servidor."""
        self.usuarios.append(usuario)
        usuario.servidor = self

    def conectar(self, otro_servidor):
        """Conecta dos servidores (grafo no dirigido)."""
        if otro_servidor not in self.conexiones:
            self.conexiones.append(otro_servidor)
            otro_servidor.conexiones.append(self)

    def recibir_mensaje(self, mensaje):
        """Recibe un mensaje y lo agrega a la cola correspondiente."""
        if hasattr(mensaje, 'urgente') and mensaje.urgente:
            heapq.heappush(self.cola_prioridad, (0, mensaje))
        else:
            self.mensajes.append(mensaje)

    def procesar_mensajes(self):
        """Procesa primero los mensajes urgentes, luego los normales."""
        # Procesar los urgentes (cola de prioridad)
        while self.cola_prioridad:
            _, mensaje = heapq.heappop(self.cola_prioridad)
            self.entregar_mensaje(mensaje)

        # Procesar los normales (FIFO)
        while self.mensajes:
            mensaje = self.mensajes.pop(0)
            self.entregar_mensaje(mensaje)

    def entregar_mensaje(self, mensaje):
        """Entrega el mensaje al usuario destino o lo reenvía a otro servidor."""
        if mensaje.destino.servidor == self:
            mensaje.destino.recibir_mensaje(mensaje)
        else:
            ruta = self.buscar_ruta_bfs(mensaje.destino.servidor)
            if ruta and len(ruta) > 1:
                siguiente = ruta[1]
                siguiente.recibir_mensaje(mensaje)

    def buscar_ruta_bfs(self, destino):
        """Busca una ruta entre servidores usando BFS (Breadth-First Search)."""
        visitados = set()
        cola = deque([[self]])
        while cola:
            camino = cola.popleft()
            nodo = camino[-1]
            if nodo == destino:
                return camino
            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in nodo.conexiones:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)
        return None

    def buscar_ruta_dfs(self, destino, visitados=None, camino=None):
        """Busca una ruta entre servidores usando DFS (Depth-First Search)."""
        if visitados is None:
            visitados = set()
        if camino is None:
            camino = [self]
        if self == destino:
            return camino
        visitados.add(self)
        for vecino in self.conexiones:
            if vecino not in visitados:
                nuevo_camino = camino + [vecino]
                resultado = vecino.buscar_ruta_dfs(destino, visitados, nuevo_camino)
                if resultado:
                    return resultado
        return None
