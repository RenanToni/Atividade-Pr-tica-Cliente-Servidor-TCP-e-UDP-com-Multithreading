import socket
import threading
import time

def processar_udp(servidor, dados, endereco):
    # Simula processamento
    time.sleep(2)
    servidor.sendto("Resposta do servidor UDP".encode(), endereco)
    print(f"[UDP] Resposta enviada para: {endereco}")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind(('127.0.0.1', 6000))
    print("[UDP] Servidor aguardando pacotes na porta 6000...")

    while True:
        dados, endereco = servidor.recvfrom(1024)
        # Dispara thread para processar a resposta sem travar o loop de recebimento
        thread = threading.Thread(target=processar_udp, args=(servidor, dados, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()