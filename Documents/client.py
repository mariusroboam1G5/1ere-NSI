# Créé par MARIUS.ROBOAM, le 16/05/2023 en Python 3.7
#client UDP
import socket

UDP_IP_DU_BINOME = "127.0.0.1"   #adresse de la machine du binôme (à adapter)
UDP_PORT_DU_BINOME = 5000        #port de la machine du binôme (à adapter)

# Crée un socket UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = 'nsi'
octets = message.encode("Utf8")
print(octets)
sock.sendto(octets, (UDP_IP_DU_BINOME, UDP_PORT_DU_BINOME))
