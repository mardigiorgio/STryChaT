# Chat App

## Introduction

This repository contains a simple client-server chat application implemented in Python using sockets and threading. The application allows two users to communicate with each other over a network. The client side and server side are implemented in separate scripts: `client.py` and `server.py` respectively.

## Features

- Real-time communication between a client and a server.
- User-friendly interface with a colorful banner.
- Customizable alias for the client.

## Usage

### Prerequisites

Make sure you have Python installed on your system.

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/xdmahko/STryChaT.git

2. **Navigate to the project directory:**

   ```bash
   cd STryChaT

3. **Install the required dependencies:**

   ```bash
   pip install termcolor

### Running the Server

1. **Open a terminal and navigate to the project directory.**
2. **Run the server script:**

   ```bash
   python server.py

The server will bind to the default address ('', 11111).
3. **Wait for the server to establish a connection with a client.**

### Running the Client

1. **Open a new terminal and navigate to the project directory.**
2. **Run the client script:**

   ```bash
   python client.py

3. **Run the client script:**
- Enter your desired alias.
- Provide the target server's IP address and port.
4. **Start chatting!**

## Exiting

To exit the chat, type exit and press Enter in the client terminal.

## Known Issues

Document any known issues or limitations of the current implementation.

## Contributing

Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests.

## License

This project is licensed under the MIT License.
   