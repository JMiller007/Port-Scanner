# Port Scanner

This project is a simple port scanner application that allows you to scan a range of ports on a specified IP address to determine which ports are open. This can be useful for network security and management.

## Features
- Scan a range of ports on a specified IP address
- Display the list of open ports
- Provide feedback during the scanning process
- Simple and intuitive graphical user interface (GUI) using `tkinter`

## Requirements
- Python 3.x

## How to Run the Application
1. **Clone the Repository**:
    ```sh
    git clone https://github.com/your-username/port-scanner.git
    cd port-scanner
    ```

2. **Install Required Packages**:
    Ensure you have `tkinter` installed. It usually comes pre-installed with Python, but if not, you can install it using:
    - On Debian-based systems (like Ubuntu):
      ```sh
      sudo apt-get install python3-tk
      ```
    - On macOS:
      ```sh
      brew install python-tk
      ```
    - On Windows, `tkinter` is included with the standard Python installation.

3. **Run the Application**:
    ```sh
    python port_scanner.py
    ```

## How to Test the Application
To verify that the port scanner is working correctly, you can open a specific port on your computer and scan for it using the application.

1. **Open a Terminal or Command Prompt**.
2. **Navigate to a Directory**:
    ```sh
    cd path/to/any/directory
    ```

3. **Start a Simple HTTP Server**:
    ```sh
    python -m http.server 8000
    ```
    This will open port 8000.

4. **Run the Port Scanner Application**:
    - Enter your local IP address in the IP address field (you can find this using `ipconfig` on Windows or `ifconfig` on macOS/Linux).
    - Set the start port to `8000` and the end port to `8000`.
    - Click "Start Scan".

5. **Verify the Results**:
    The application should display that port 8000 is open.

## Explanation of Terms
- **IP Address**: The address of the computer you are scanning. It identifies a device on a network.
- **Port**: A virtual point where network connections start and end. Think of it as a door that data can pass through.
- **Port Range**: The range of ports you want to scan. For example, ports 20 to 80.
- **Open Port**: A port that is accepting connections, meaning it's accessible and listening for traffic.

## Limitations
- This port scanner is designed for educational purposes and basic network management tasks. It may not include all features required for advanced network security analysis.
- Ensure you have permission to scan the IP addresses and ports you are targeting.
