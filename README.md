# Joker-Eye
Joker-Eye is a lightweight network scanning tool for Python. Quickly scan open/closed ports on a target host with easy installation using git clone. Discover potential vulnerabilities in your network effortlessly.

```
# Joker-Eye Network Scanner

Joker-Eye is a simple and efficient network scanning tool written in Python. It allows you to scan open and closed ports on a target host to assess potential vulnerabilities in your network. The tool provides an easy installation process using `git clone`, making it accessible and ready for use in no time.

## Features

- Scan open and closed ports on a target host
- Identify potential vulnerabilities in your network
- Easy installation using `git clone`
- Lightweight and efficient Python script

## Requirements

- Python 3.x
- Internet connectivity for accessing target hosts

# Joker Eye Port Scanner (by Kalki-Dev)

![Joker Eye(https://i.ibb.co/bRVPNbV/IMG-20230726-215243.jpg)]



## Introduction
Joker Eye Port Scanner is a command-line tool designed to scan for open or closed ports on a target host. It provides various scanning options and displays the results for each scanned port.

## Features
- Fast and efficient port scanning
- Multiple scanning options:
  - Scan all ports (1 to 1024)
  - Scan all ports (1 to 65000)
  - Scan an individual port
  - Scan a range of ports (start value to end value)
- Colorful and visually appealing user interface

## Requirements
- Python 3.x
- `colorama` library (You can install it using `pip install colorama`)

## Usage
1. Clone the repository or download the `joker_eye.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where `joker_eye.py` is located.
4. Run the script using the command: `python joker_eye.py`

## Instructions
1. When the tool starts, it will display the Joker Eye banner.
2. Enter the target host's IP address or domain name.
3. Choose a scanning option from the menu:
   - `1`: Scan all ports from 1 to 1024.
   - `2`: Scan all ports from 1 to 65000.
   - `3`: Scan an individual port of your choice.
   - `4`: Scan a range of ports (start value to end value).
   - `exit`: To close the script and exit the tool.
4. The tool will display the scan results for each port on the target host.
5. To exit the tool, select the `exit` option.

## Example
```
$ python joker_eye.py

================ JOKER EYE PORT SCANNER =================

Enter the target host: 127.0.0.1

1. Scan all ports (1 to 1024)
2. Scan all ports (1 to 65000)
3. Scan an individual port
4. Scan a range of ports (start value to end value)
exit. Exit the script

Enter the option number or 'exit' to close: 1

Scanning ports...

Port 80 is open
Port 443 is closed
Port 8080 is closed
...

================ Scanning completed in 2.34 seconds =================

Enter the option number or 'exit' to close: exit

Closing the script... Goodbye!
```

## Disclaimer
This tool is intended for educational purposes only. The authors, contributors, and maintainers of this tool are not responsible for any unauthorized use, misuse, or damage caused by this tool. Use at your own risk.

## Credits
This tool was created by Kalki-Dev. You can find more projects and information on GitHub: [https://github.com/Kalki-Dev](https://github.com/Kalki-Dev)

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as per the terms of the license.
