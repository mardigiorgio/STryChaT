# socket-chat

socket-chat is a lightweight client–server chat application written in Python. It
demonstrates basic socket programming and threading by enabling two terminals to
exchange messages in real time.

## Features

- Text‑based chat between a server and a single client
- Customisable user alias for the client
- Colourful terminal banner (requires [`termcolor`](https://pypi.org/project/termcolor/))

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` for dependency installation

Install the required dependency:

```bash
pip install termcolor
```

### Running the server

```bash
python server.py
```

The server listens on port `11111` by default and waits for a client to connect.

### Running the client

```bash
python client.py
```

When prompted:

1. Enter an alias to identify yourself in the chat.
2. Provide the server's IP address and port (use `localhost` and `11111` if
   running locally).

Once connected, messages typed in the client terminal will appear on the server
terminal and vice versa.

### Exiting

Type `exit` in the client terminal to end the chat session gracefully.

## Contributing

Pull requests, bug reports and feature suggestions are welcome.

## License

This project is released under the MIT License.

