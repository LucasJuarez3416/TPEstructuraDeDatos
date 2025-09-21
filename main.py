from datetime import datetime

# Clase Mensaje
class Mensaje:
    def __init__(self, remitente, destinatario, asunto, cuerpo):
        self.__remitente = remitente
        self.__destinatario = destinatario
        self.__asunto = asunto
        self.__cuerpo = cuerpo
        self.__fecha = datetime.now()

    # Getters (propiedades)
    @property
    def remitente(self):
        return self.__remitente

    @property
    def destinatario(self):
        return self.__destinatario

    @property
    def asunto(self):
        return self.__asunto

    @property
    def cuerpo(self):
        return self.__cuerpo

    @property
    def fecha(self):
        return self.__fecha

    def mostrar_resumen(self):
        return f"[{self.__fecha.strftime('%d/%m/%Y %H:%M')}] De: {self.__remitente} | Asunto: {self.__asunto} | Cuerpo: {self.__cuerpo}"



# Clase Carpeta
class Carpeta:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__mensajes = []

    @property
    def nombre(self):
        return self.__nombre

    def agregar_mensaje(self, mensaje):
        self.__mensajes.append(mensaje)

    def listar_mensajes(self):
        return [msg.mostrar_resumen() for msg in self.__mensajes]


# Clase Usuario
class Usuario:
    def __init__(self, nombre, email, password):
        self.__nombre = nombre
        self.__email = email
        self.__password = password
        self.__bandeja_entrada = Carpeta("Bandeja de entrada")

    @property
    def email(self):
        return self.__email

    def recibir_mensaje(self, mensaje):
        self.__bandeja_entrada.agregar_mensaje(mensaje)

    def listar_inbox(self):
        return self.__bandeja_entrada.listar_mensajes()


# Clase ServidorCorreo
class ServidorCorreo:
    def __init__(self):
        self.__usuarios = {}

    def registrar_usuario(self, usuario):
        self.__usuarios[usuario.email] = usuario

    def enviar_mensaje(self, remitente, destinatario_email, asunto, cuerpo):
        if destinatario_email in self.__usuarios:
            mensaje = Mensaje(remitente, destinatario_email, asunto, cuerpo)
            self.__usuarios[destinatario_email].recibir_mensaje(mensaje)
            print(f"Mensaje enviado a {destinatario_email} por {remitente} ")
        else:
            print("Error: destinatario no registrado en el servidor.")




#PRueba
if __name__ == "__main__":
    # Crear servidor
    servidor = ServidorCorreo()


    # Crear usuarios
    Lucas = Usuario("Lucas Juárez", "lucas@mail.com", "123")
    Jorge = Usuario("Jorge Ordonez", "jorge@mail.com", "567")
    Pablo = Usuario("Pablo Hoyos", "pablo@mail.com","890")

    # Registrar usuarios en el servidor
    servidor.registrar_usuario(Lucas)
    servidor.registrar_usuario(Jorge)
    servidor.registrar_usuario(Pablo)

    # Enviar un mensaje de Lucas a Jorge
    servidor.enviar_mensaje("lucas@mail.com", "jorge@mail.com", "Hola", "¿Cómo estás?")
    servidor.enviar_mensaje("lucas@mail.com", "pablo@mail.com", "Hola2", "¿Cómo estás?2")

    # Ver mensajes recibidos por Jorge
    print("Mensajes en la bandeja de entrada de Jorge:")
    for mensaje in Jorge.listar_inbox():
        print(mensaje)

    # Ver mensajes recibidos por Jorge
    print("Mensajes en la bandeja de entrada de Pablo:")
    for mensaje in Pablo.listar_inbox():
        print(mensaje)    

