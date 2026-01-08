from socket import socket, AF_INET, SOCK_STREAM


def request_current_from_ammeter(port: int, command: bytes) -> float:
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(('localhost', port))
        s.sendall(command)
        data = s.recv(1024)
        if data:
            print(f"Received current measurement from port {port}: {data.decode('utf-8')} A")
            return float(data.decode("utf-8").strip())
        else:
            print("No data received.")

