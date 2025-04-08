# Primero se instala paramiko con el siguiente comando "pip install paramiko"
import paramiko

#En las siguientes lineas, se crean las variables necesarias
#Acontinuacion se guarda la ip del dispositivo final de la conexion ssh, el puerto y el usuario y contraseña
host = "192.168.0.10"
puerto = 22
nombre_usuario = "root"
contraseña = "root"

comando = "pwd"

#En el siguiente codigo se ingresa la informacion a la variable ssh para por ultimo ingresar la variable comando cuando ya haya conexion
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, puerto, nombre_usuario, contraseña)
stdia, stdout, stderr = ssh.exec_command(comando)
lines = stdout.readlines()
print(lines)









