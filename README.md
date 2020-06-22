# notecard-throughput-tester
Python Script for testing a Serial connection between a RPI and Notecard

## Usage

- Before running, make sure to configure the UART connection on your Raspberry Pi in accordance with [this doc](https://www.raspberrypi.org/documentation/configuration/uart.md).

- Download the `note-python` library and use scp to copy the contents of the `notecard` directory to the development folder on your Pi

```bash
scp -r ~/Development/blues/note-python/notecard pi@bluepi.local:dev/notecard-throughput-tester/notecard/
```