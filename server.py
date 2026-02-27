import socket
import threading
#HOST = "127.0.0.1"
HOST = "server"
PORT = 65432


"""with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode()}")
            response = f"Echo: {data.decode()}"
            conn.sendall(response.encode())"""

def client_handling(conn, addr):
     print(f"Connected by {addr}")
     with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            msg = data.decode(errors="replace")
            print(f"Received from {addr}:{msg}")
            response = f"Echo: {msg}"
            conn.sendall(response.encode())
#print(f"Connection closed by {addr}")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server is listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=client_handling, args=(conn, addr), daemon=True)
            t.start()

if __name__ == "__main__":
    main()

