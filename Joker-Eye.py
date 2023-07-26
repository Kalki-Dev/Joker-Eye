import socket
import time
import os

def print_banner():
    banner = (

        "\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m\n"                                        "\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⠀⢰⡆⢘⣆⠀⠀⡆⠀⢸⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m\n"
        "\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⣆⣧⡤⠾⢷⡚⠛⢻⣏⢹⡏⠉⣹⠟⡟⣾⠳⣼⢦⣀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m\n"                                         "\033[1;32m⠀⠀⠀⠲⣄⣤⣞⡉⠛⢶⣾⡷⠟⣿⣿⣿⣿⣿⣿⣿⣾⣷⣼⣽⣽⣿⣯⡾⢃⣠⣞⠟⠓⢦⣀⠆⠀⠀⡀⠀⠀⠀⠀⠀⠀\033[0m\n"
        "\033[1;32m⠀⠀⢤⣀⣜⣉⣩⣽⠿⠋⠀⠀⣸⠯⠈⠀⠁⣴⣿⣿⣿⡶⠤⠽⣇⠈⣿⠀⠀⠈⠙⠻⢶⣾⣻⣭⠿⢫⣀⣴⡶⠃⠀⠀\033[0m\n"
        "\033[1;32m⠀⠀⠤⠬⢭⣿⣿⠋⠀⠀⠀⠀⢻⡀⠀⠀⠀⢸⣿⣿⣿⡿⠋⠁⠀⠀⣼⠁⠀⠀⠀⠀⠀⠘⠛⢶⣶⣾⣻⡯⠄⠀⣠⠄\033[0m\n"
        "\033[1;32m⡔⢀⡵⠋⢧⢹⡀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⣠⣾⣿⡛⠛⠛⠓⠦⠀⠀⠀⠀\033[0m\n"
        "\033[1;32m⣇⠘⠳⠦⠼⠧⠷⣄⣀⠀⠀⠀⠀⠀⠀⠳⢤⣀⠀⠀⠀⠀⠀⢀⣠⠾⠃⠀⠀⠀⣀⣴⣻⣟⡋⠉⠉⢻⠶⠀⠀⠀⠀⠀⠀\033[0m\n"
        "\033[1;32m⠈⠑⠒⠒⠀⠀⢄⣀⡴⣯⣵⣖⣦⠤⣀⣀⣀⠉⠙⠒⠒⠒⠚⠉⢁⣀⣠⢤⣖⣿⣷⢯⡉⠉⠙⣲⠞⠁⠀⠀⠀⠀⠀⠀⠀\033[0m\n"
        "\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠈⠙⠣⢤⡞⠉⢉⡿⠒⢻⢿⡿⠭⣭⡭⠿⣿⡿⠒⠻⣯⡷⡄⠉⠳⣬⠷⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m\n"                                        "\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠺⠤⣄⣠⡏⠀⠀⡿⠀⠀⠘⡾⠀⢀⣈⡧⠴⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m\n"
        "\033[1;32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠒⠓⠒⠒⠚⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m\n"
        "\033[1;32m      _       _                  _____         \n"
        "\033[1;31m     | | ___ | | _____ _ __     | ____|   _  ___\n"
        "\033[1;34m  _  | |/ _ \| |/ / _ \ '__|____|  _|| | | |/ _ \n"
        "\033[1;34m | |_| | (_) |   <  __/ | |_____| |__| |_| |  __/\n"
        "\033[1;32m  \___/ \___/|_|\_\___|_|       |_____\\__, |\___|\n"
        "\033[0m                                          |___/\n"

"\033[1;35m| Version: 1.2.4 \033[0m\n"
   "\033[1;33m| Tool Created By GSBORA (Kalki-Dev)   \033[0m\n"

   )
    print(banner)
if __name__ == "__main__":
    print_banner()


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
    host = input("Enter the target host: ")
    port_input = input("Enter the port number(s) to scan (separated by spaces): ")

    try:
        ports = [int(port) for port in port_input.split()]
    except ValueError:
        print("Invalid port numbers. Please provide space-separated integers.")
        return

    start_time = time.time()

    for port in ports:
        scan_port(host, port)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Scanning completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    joker_eye_scan()
