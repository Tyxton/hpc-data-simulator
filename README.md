This is a Python-based utility designed to simulate high-frequency hardware data ingestion, unpacking, and logging.

For this project, I designed to use big-endian struct mapping since it is standard for network topolgy, rather than hardware which would've been little-endian.

| Offset (Bytes) | Size(Bytes) | Data Type | Field Name |
| :------------- | :---------- | :-------- | :--------- |
| 0-3            | 4           | uint32    | Timestamp  |
| 4-5            | 2           | char[2]   | SensorID   |
| 6-7            | 2           | uint16    | Sequence   |
| 8-15           | 8           | double    | Reading    |

This is meant to simulate a 16-byte packet giving the unix timestamp, the sensor-ID read, the sequence of data given, and the sensor reading.

This is designed to be ran "over-network" simulated locally via TCP binding, reciever.py is the listening server, while sender.py is the raw datastream.

---

# How to use:

- Open two terminal sessions
- On the first terminal, start the reciever `python3 reciever.py` it will then wait for incoming data.
- On the second terminal, start the sender `python3 sender.py`, it will immediately start sending mock data to the reciever.
- To cancel, you can start either with reciever.py or sender.py with the keyboard interrupt: `Ctrl+C`.

---

# Purpose of this Project

This simulates real-world data processing like wind tunnel telemetry or industrial IoT monitoring where sensors, or low-voltage systems are sending raw data streams to be processed for use, interpretation, and logging.
