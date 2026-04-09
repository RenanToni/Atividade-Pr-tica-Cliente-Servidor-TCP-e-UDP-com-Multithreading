import socket
import threading
import time

def lidar_com_cliente(conexao, endereco):
    print(f"[TCP] Novo cliente conectado: {endereco}")
    time.sleep(2)
    conexao.send("Resposta do servidor TCP".encode())
    conexao.close()
    print(f"[TCP] Atendimento finalizado para: {endereco}")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('127.0.0.1', 5000))
    servidor.listen(100) # Fila de espera
    print("[TCP] Servidor aguardando conexões na porta 5000...")

    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()