import socket
import threading

def disparar_requisicao(id_cliente):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    cliente.sendto(f"Ola cliente {id_cliente}".encode(), ('127.0.0.1', 6000))
    dados, _ = cliente.recvfrom(1024)
    print(f"Cliente {id_cliente} recebeu: {dados.decode()}")

def teste_carga(n):
    threads = []
    for i in range(n):
        t = threading.Thread(target=disparar_requisicao, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    teste_carga(50)