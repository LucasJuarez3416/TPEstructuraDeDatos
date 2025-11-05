# Entrega 3 - Algoritmos y Funcionalidades Avanzadas

## Filtros automáticos con listas y diccionarios
El sistema de correo utiliza listas y diccionarios para organizar los mensajes recibidos y enviados por cada usuario y servidor.
Los filtros permiten clasificar mensajes según su tipo, origen o prioridad.

## Cola de prioridades para mensajes urgentes
Se implementó una cola de prioridad con `heapq` para asegurar que los mensajes marcados como `urgente=True` sean procesados antes que los mensajes normales.

## Grafo de servidores y envío de mensajes
La red de servidores se modela como un grafo no dirigido, donde cada nodo es un servidor y cada conexión representa una arista.
El envío de mensajes se simula utilizando dos algoritmos clásicos de búsqueda:

- **BFS (Breadth-First Search)**: utilizado para encontrar la ruta más corta entre servidores.
- **DFS (Depth-First Search)**: implementado como alternativa para explorar rutas posibles en profundidad.

Ambos métodos se implementan en la clase `ServidorCorreo` y se utilizan internamente durante la entrega de mensajes.
