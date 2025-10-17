# TPEstructuraDeDatos
 
Grupo conformado por:
Lucas Juárez, Jorge Ordonez y Pablo Hoyos.


En este proyecto implementamos un sistema de correo electrónico básico utilizando (POO)

Definimos las clases principales: Mensaje, Carpeta, Usuario; y ServidorCorreo.

CLases principales:

 (Mensaje) 

        Atributos privados:

        __remintente: dirección del emisor del mensaje.
        __destinatario: direccion del receptor.
        __asunto: titulo del mensaje.
        __cuerpo: contenido del mensaje.
        __fecha: fecha y hora en que se crea el mensaje. La obtenemos usando (datetime.now()), metodo de la clase "datetime del modulo "datetime" que importamos en la linea 1.


        métodos y propiedades: 

        (@property) permite leer los atributos, pero no modificarlos por fuera de la clase.

        mostrar_resumen(): nos devuelve un string con la fecha, remitente, asunto y cuerpo resumidos.

    
    (Carpeta) contiene mensajes, funciona como bandeja de entrada.

        Atributos privados: __nombre , __mensajes

        métodos y propiedades:

        agregar_mensajes(mensaje) almacena mensajes en la carpeta.
        listar_mensajes() devuelve los resúmenes de los mensajes almacenados.

        nombre: permite leer el nombre de la carpeta

    (Usuario)
        representa un usuario del sistema.
        
        Atributos privados:
        
        __nombre
        __email
        __password
        __bandeja de entrada

        metodos y propiedades: 

        email permite acceder al correo electrónico del usuario.

        recibir_mensaje(mensaje) añade un mensaje a la bandeja de entrada.
        listar_inbox() muestra los mensajes recibidos.

    (ServidorCorreo) Administra usuarios y el envio de mensajes.

        Atributos privados: __usuarios diccionario de usuarios registrados.

        métodos:

        registrar_usuario(usuario) agrega un usuario al servidor.
        enviar_mensaje(remitente, destinatario, asunto, cuerpo) crea un mensaje y lo entrega al destinatario. Solo si existe.


    Flujo de funcionamiento:
    
    1- Se crea un ServidorCorreo.
    2- Se registran uno o varios usuarios.
    3- Un usuario envia un mensaje a otro usando servidor.enviar_mensaje
    4- El servidor crea un objeto Mensaje y lo coloca en la carpeta "bandeja de entrada" del destinatario
    5- El destinatario puede listar sus mensajes con listar_inbox()
    