# Informe de Entrega 2  
### Estructuras de Datos y Recursividad  
**Materia:** Algoritmos y Estructuras de Datos – UNaB  
**Grupo:** 55  
**Integrantes:** Lucas Juárez, Pablo Hoyos, Jorge Ordoñez  

---

## Objetivo de la entrega
Implementar la gestión recursiva de carpetas y subcarpetas dentro de un cliente de correo electrónico en Python, aplicando estructuras de datos en forma de árbol general, junto con búsquedas y operaciones recursivas.  

El sistema debía permitir:  
- Crear carpetas y subcarpetas de forma jerárquica.  
- Mover mensajes entre carpetas.  
- Buscar mensajes de manera recursiva (por asunto o remitente).  
- Analizar la eficiencia de las operaciones implementadas.  

---

## ⚙️ Diseño general del sistema

El sistema está implementado mediante una arquitectura orientada a objetos y modularizada, compuesta por los siguientes módulos principales:

| Módulo               | Descripción                                                                                                   |
|----------------------|---------------------------------------------------------------------------------------------------------------|
| `mensaje.py`         | Define la clase `Mensaje`, que modela un correo con remitente, destinatario, asunto, cuerpo y fecha.          |
| `carpeta.py`         | Implementa la clase `Carpeta`, que representa un nodo del árbol (carpeta) y contiene subcarpetas y mensajes.  |
| `usuario.py`         | Modela a un usuario del sistema con su estructura de carpetas y funcionalidades para buscar y mover mensajes. |
| `servidor_correo.py` | Gestiona los usuarios y la comunicación entre ellos.                                                          |
| `pyinterfaces/`      | Contiene las interfaces abstractas (ABC) que definen los métodos obligatorios para cada clase.                |

---

## Estructura recursiva (árbol general)

La clase `Carpeta` fue rediseñada para comportarse como un nodo de un árbol general.  
Cada carpeta puede contener:
- una lista de **mensajes**, y  
- una lista de **subcarpetas** (cada una es otra instancia de `Carpeta`).  

### Ejemplo visual:
```
Bandeja de entrada
├── Trabajo
│   ├── Proyectos
│   └── Reuniones
└── Familia
```

Cada subcarpeta conoce a su **carpeta padre**, lo que permite recorrer el árbol en ambos sentidos (hacia arriba o hacia abajo).  

---

## Operaciones implementadas con recursividad

| Método                             | Descripción                                                     | Tipo de recursividad |
|------------------------------------|-----------------------------------------------------------------|----------------------|
| `obtener_subcarpeta(nombre)`       | Busca una carpeta por nombre recorriendo todas las subcarpetas. | Recursividad directa |
| `buscar_mensajes_recursivo(texto)` | Recorre todo el árbol y devuelve los mensajes cuyo asunto o remitente coincidan con el texto buscado. | Recursividad directa |
| `mostrar_estructura(nivel=0)`      | Muestra el árbol jerárquico de carpetas con indentación según el nivel. | Recursividad directa |

Ejemplo de salida:
```
- Bandeja de entrada
  - Trabajo
    - Proyectos
  - Familia
```

---

## Operaciones implementadas

- **Agregar subcarpeta:** `agregar_subcarpeta(nombre)`  
- **Buscar carpeta (recursivo):** `obtener_subcarpeta(nombre)`  
- **Mover mensaje:** `mover_mensaje(mensaje, carpeta_destino)`  
- **Buscar mensajes recursivamente:** `buscar_mensajes_recursivo(texto)`  
- **Mostrar estructura del árbol:** `mostrar_estructura()`  

---



## Conclusiones

- Se logró implementar una estructura recursiva de carpetas utilizando una relación de composición entre instancias de la clase `Carpeta`.  
- Se aplicaron principios de recursión, modularidad y encapsulamiento.  
- Las búsquedas y recorridos del árbol demuestran un uso correcto de la recursividad directa.  
- La organización modular y la documentación mejoraron significativamente respecto a la primera entrega.  
- El diseño es fácilmente extensible para la próxima etapa (filtros automáticos y grafos de servidores).  

---
