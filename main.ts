radio.onReceivedString(function (receivedString) {
    MENSAJE_CIFRADO = receivedString
    basic.showString(MENSAJE_CIFRADO)
    decifrar()
    basic.showString("-")
    basic.showString(MENSAJE_DECIFRADO)
})
function cifrar () {
    MENSAJE_CIFRADO = ""
    for (let index = 0; index <= MENSAJE.length; index++) {
        if (MENSAJE.substr(index, 1) == "") {
            MENSAJE_CIFRADO = "" + MENSAJE_CIFRADO + " "
        } else {
            for (let index2 = 0; index2 <= ABECEDARIO.length; index2++) {
                if (MENSAJE.substr(index, 1) == ABECEDARIO.substr(index2, 1)) {
                    MENSAJE_CIFRADO = "" + MENSAJE_CIFRADO + ABECEDARIO_INVERTIDO.substr(index2, 1)
                    index2 = ABECEDARIO.length
                }
            }
        }
    }
}
function decifrar () {
    MENSAJE_DECIFRADO = ""
    for (let index = 0; index <= MENSAJE_CIFRADO.length; index++) {
        if (MENSAJE_CIFRADO.substr(index, 1) == "") {
            MENSAJE_DECIFRADO = "" + MENSAJE_DECIFRADO + " "
        } else {
            for (let index2 = 0; index2 <= ABECEDARIO_INVERTIDO.length; index2++) {
                if (MENSAJE_CIFRADO.substr(index, 1) == ABECEDARIO_INVERTIDO.substr(index2, 1)) {
                    MENSAJE_DECIFRADO = "" + MENSAJE_DECIFRADO + ABECEDARIO.substr(index2, 1)
                    index2 = ABECEDARIO_INVERTIDO.length
                }
            }
        }
    }
}
input.onButtonPressed(Button.A, function () {
    MENSAJE = "HOLA"
    basic.showString(MENSAJE)
    cifrar()
    basic.showString("-")
    basic.showString(MENSAJE_CIFRADO)
    radio.sendString(MENSAJE_CIFRADO)
})
let MENSAJE = ""
let MENSAJE_DECIFRADO = ""
let MENSAJE_CIFRADO = ""
let ABECEDARIO_INVERTIDO = ""
let ABECEDARIO = ""
radio.setGroup(15)
ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ABECEDARIO_INVERTIDO = ""
for (let index = 0; index <= ABECEDARIO.length; index++) {
    ABECEDARIO_INVERTIDO = "" + ABECEDARIO_INVERTIDO + ABECEDARIO.substr(ABECEDARIO.length - index, 1)
}
basic.forever(function () {
	
})
