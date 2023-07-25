import socket
import sys
import time

def scan_port(host, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt (in seconds)
        sock.settimeout(1)
        # Attempt to connect to the specified host and port
        result = sock.connect_ex((host, port))

        # Check the connection result
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

        # Close the socket
        sock.close()
    except socket.error:
        print(f"Error connecting to port {port}")

def joker_eye_scan():
    if len(sys.argv) < 2:
        print("Usage: python joker_eye.py <host> [port1 port2 ...]")
        sys.exit(1)

    host = sys.argv[1]
    ports = [int(port) for port in sys.argv[2:]] if len(sys.argv) > 2 else range(1, 1025)

    start_time = time.time()

    for port in ports:
        scan_port(host, port)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Scanning completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    joker_eye_scan()
