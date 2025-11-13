import zmq
import zmq.asyncio


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*.5555")

    while True:
        message = socket.recv()

        print(f"Received: {message}")
        socket.send_string("Working?")


if __name__ == "__main__":
    main()
