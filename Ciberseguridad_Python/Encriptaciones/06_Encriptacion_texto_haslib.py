# pip install hashlib

import hashlib

def main():
    #Se solicita una palabra por medio de input y se transforma en string con el str, esto se guarda en la variable palabra
    palabra = str(input("Ingrese la palabra a encriptar: "))

    #La primer conversion es a md5, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    md5 = hashlib.md5(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash MD5: " + md5)

    #La siguiente conversion es a sha1, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    sha1 = hashlib.sha1(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha1: " + sha1)

    #La siguiente conversion es a sha224, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    sha224 = hashlib.sha224(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha224: " + sha224)

    #La siguiente conversion es a sha256, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    sha256 = hashlib.sha256(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha256: " + sha256)

    #La siguiente conversion es a sha384, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    sha384 = hashlib.sha384(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha384: "+ sha384)

    #La siguiente conversion es a sha512, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    sha512 = hashlib.sha512(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha512: "+ sha512)

    #Añadidos desde python 3.6 en adelante
    #La siguiente conversion es a blake2b, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    blake2b = hashlib.blake2b(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash blake2b: "+ blake2b)

    #La siguiente conversion es a blake2s, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    blake2s = hashlib.blake2s(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash blake2s: "+ blake2s)

    #La siguiente conversion es a sha3_224, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    sha3_224 = hashlib.sha3_224(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha3_224: "+ sha3_224)

    #La siguiente conversion es a sha3_256, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    sha3_256 = hashlib.sha3_256(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha3_256: "+ sha3_256)

    #La siguiente conversion es a sha3_384, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    sha3_384 = hashlib.sha3_384(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha3_384: "+ sha3_384)

    #La siguiente conversion es a sha3_512, la variable se vuelve hexadecimal el codigo con caracteristica UTF-8 y luego se muestra en pantalla la repuesta
    sha3_512 = hashlib.sha3_512(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha3_512: "+ sha3_512)

if __name__== "__main__":
    main()





