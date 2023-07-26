import socket
import time
from colorama import Fore, Style

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

        start_time = time.time()

        # Attempt to connect to the specified host and port
        result = sock.connect_ex((host, port))

        end_time = time.time()
        elapsed_time = end_time - start_time

        # Check the connection result
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

        # Close the socket
        sock.close()
        print(f"Time taken for port {port}: {elapsed_time:.2f} seconds")
    except socket.error:
        print(f"{Fore.RED}Error connecting to port {port}{Style.RESET_ALL}")

def joker_eye_scan():
    print(f"{Fore.CYAN}{'='*15} JOKER EYE PORT SCANNER {'='*14}{Style.RESET_ALL}\n")
    host = input("Enter the target host: ")

    options = {
        '1': "Scan all ports (1 to 1024)",
        '2': "Scan all ports (1 to 65000)",
        '3': "Scan an individual port",
        '4': "Scan a range of ports (start value to end value)",
        'exit': "Exit the script"
    }

    while True:
        for key, value in options.items():
            print(f"{Fore.YELLOW}{key}. {value}{Style.RESET_ALL}")

        option = input("Enter the option number or 'exit' to close: ")

        if option == 'exit':
            print(f"{Fore.CYAN}Closing the script... Goodbye!{Style.RESET_ALL}")
            break

        if option == '1':
            start_port = 1
            end_port = 1024
        elif option == '2':
            start_port = 1
            end_port = 65000
        elif option == '3':
            port_input = input("Enter the individual port number: ")
            try:
                start_port = int(port_input)
                end_port = start_port
            except ValueError:
                print(f"{Fore.RED}Invalid port number. Please provide a valid integer.{Style.RESET_ALL}")
                continue
        elif option == '4':
            start_port_input = input("Enter the start port value: ")
            end_port_input = input("Enter the end port value: ")
            try:
                start_port = int(start_port_input)
                end_port = int(end_port_input)
            except ValueError:
                print(f"{Fore.RED}Invalid port numbers. Please provide valid integers.{Style.RESET_ALL}")
                continue
        else:
            print(f"{Fore.RED}Invalid option. Please choose a valid option.{Style.RESET_ALL}")
            continue

        start_time = time.time()

        print(f"\n{Fore.GREEN}Scanning ports...{Style.RESET_ALL}\n")

        for port in range(start_port, end_port + 1):
            scan_port(host, port)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\n{Fore.CYAN}{'='*15} Scanning completed in {elapsed_time:.2f} seconds {'='*14}{Style.RESET_ALL}\n")

if __name__ == "__main__":
    joker_eye_scan()
