def on_received_string(receivedString):
    global MENSAJE_CIFRADO
    MENSAJE_CIFRADO = receivedString
    basic.show_string(MENSAJE_CIFRADO)
    decifrar()
    basic.show_string("-")
    basic.show_string(MENSAJE_DECIFRADO)
radio.on_received_string(on_received_string)
def cifrar():
    global MENSAJE_CIFRADO
    MENSAJE_CIFRADO = ""
    index = 0
    while index <= len(MENSAJE):
        if MENSAJE.substr(index, 1) == "":
            MENSAJE_CIFRADO = "" + MENSAJE_CIFRADO + " "
        else:
            index2 = 0
            while index2 <= len(ABECEDARIO):
                if MENSAJE.substr(index, 1) == ABECEDARIO.substr(index2, 1):
                    MENSAJE_CIFRADO = "" + MENSAJE_CIFRADO + ABECEDARIO_INVERTIDO.substr(index2, 1)
                    index2 = len(ABECEDARIO)
                index2 += 1
        index += 1
def decifrar():
    global MENSAJE_DECIFRADO
    MENSAJE_DECIFRADO = ""
    index3 = 0
    while index3 <= len(MENSAJE_CIFRADO):
        if MENSAJE_CIFRADO.substr(index3, 1) == "":
            MENSAJE_DECIFRADO = "" + MENSAJE_DECIFRADO + " "
        else:
            index22 = 0
            while index22 <= len(ABECEDARIO_INVERTIDO):
                if MENSAJE_CIFRADO.substr(index3, 1) == ABECEDARIO_INVERTIDO.substr(index22, 1):
                    MENSAJE_DECIFRADO = "" + MENSAJE_DECIFRADO + ABECEDARIO.substr(index22, 1)
                    index22 = len(ABECEDARIO_INVERTIDO)
                index22 += 1
        index3 += 1
def on_button_pressed_a():
    global MENSAJE
    MENSAJE = "HOLA"
    basic.show_string(MENSAJE)
    cifrar()
    basic.show_string("-")
    basic.show_string(MENSAJE_CIFRADO)
    radio.send_string(MENSAJE_CIFRADO)
input.on_button_pressed(Button.A, on_button_pressed_a)
MENSAJE = ""
MENSAJE_DECIFRADO = ""
MENSAJE_CIFRADO = ""
ABECEDARIO_INVERTIDO = ""
ABECEDARIO = ""
radio.set_group(15)
ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ABECEDARIO_INVERTIDO = ""
index4 = 0
while index4 <= len(ABECEDARIO):
    ABECEDARIO_INVERTIDO = "" + ABECEDARIO_INVERTIDO + ABECEDARIO.substr(len(ABECEDARIO) - index4, 1)
    index4 += 1
def on_forever():
    pass
basic.forever(on_forever)