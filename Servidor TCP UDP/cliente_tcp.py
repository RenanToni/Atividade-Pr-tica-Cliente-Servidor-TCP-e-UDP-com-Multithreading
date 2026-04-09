import socket
import threading

def disparar_requisicao(id_cliente):
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('127.0.0.1', 5000))
        resposta = cliente.recv(1024)
        print(f"Cliente {id_cliente} recebeu: {resposta.decode()}")
        cliente.close()
    except Exception as e:
        print(f"Erro no cliente {id_cliente}: {e}")

def teste_carga(n):
    threads = []
    print(f"Disparando {n} requisições simultâneas...")
    for i in range(n):
        t = threading.Thread(target=disparar_requisicao, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

if __name__ == "__main__":
    teste_carga(50)