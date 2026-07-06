# This is a byte-generator script to simulate raw machine data being sent to a local port - :7114
# This will use standard big-endian packing to simulate a real network environment.

# We want 4 seperate fields here: Timestamp, SensorID, Sequence, and Reading

import random
import struct
import time
import socket
import sys

# --- Static Sensors ---
SENSOR_OPTIONS = [b"P1", b"S2"]

# --- Sequence Generation ---
def sequence_generator():
    i = 0
    while True:
        yield i
        i = (i + 1) % 65536 # restricted to a 16-bit unsigned short limit

seqCycle = sequence_generator()

# --- Network Config ---

TCP_IP = '127.0.0.1'
TCP_PORT = 7114

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Connecting to socket at {TCP_IP}:{TCP_PORT}...")

# --- Main Hardware Simulation ---
print("Starting hardware simulation stream... press Ctrl+C to stop.")

try:
    s.connect((TCP_IP, TCP_PORT))
    print("Link established, sending mock data stream.")

    while True:
        currentTime = int(time.time())
        sensorId = random.choice(SENSOR_OPTIONS)
        sequenceNum = next(seqCycle)
        readingVal = random.uniform(0.0, 100.0)

        simPacket = struct.pack('>I2sHd', currentTime, sensorId, sequenceNum, readingVal)

        print(f"Sending Hex: {simPacket.hex()} | Size: {len(simPacket)} bytes.")
        s.sendall(simPacket)

        time.sleep(0.1)
except ConnectionRefusedError:
    print(f"\nERROR: Could not connect to {TCP_IP}:{TCP_PORT}. No server to recieve datastream.")
    s.close()
    sys.exit(1)
except KeyboardInterrupt:
    print("Sucessfully Cancelled Hardware Simulation...")
finally:
    s.close()
    print("Network Interface Released.")
