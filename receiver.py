# This is the reciever/server end of this script, this should be able to collect, parse, process, and output the incoming data from byte-form.

import socket
import struct
import time
import sys

# --- Network Config ---
TCP_IP = '127.0.0.1'
TCP_PORT = 7114

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ensures OS doesn't lock up the port

print(f"Connecting to socket at {TCP_IP}:{TCP_PORT}...")

try:
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()

    while True:
        mockData = conn.recv(16)
        
        print(f"Recieved Hex: {mockData.hex()} | Size: {len(mockData)} bytes.")

        recvPacket = struct.unpack('>I2sHd', mockData)

        print(f"{recvPacket}")
        time.sleep(0.1)

except ConnectionRefusedError:
    print(f"\nERROR: Could not connect to {TCP_IP}:{TCP_PORT}. Is the address in use?")
    s.close()
    sys.exit(1)
except KeyboardInterrupt:
    print("Sucessfully Cancelled Hardware Simulation...")
finally:
    s.close()
    print("Network Interface Released.")


