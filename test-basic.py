import sys
import argparse
import time

from periphery import Serial
import notecard

port = Serial("/dev/serial0", 9600)
card = notecard.OpenSerial(port)

if card.uart is not None:
  print("Notecard connected...")

def send_request(req):
  try:
      rsp = card.Transaction(req)
      
      return rsp
  except Exception as exception:
      print("transaction error: " + ExceptionInfo(exception))

def ExceptionInfo(exception):
    s1 = '{}'.format(sys.exc_info()[-1].tb_lineno)
    s2 = exception.__class__.__name__
    return "line " + s1 + ": " + s2 + ": " + ' '.join(map(str, exception.args))

def main():
    print("Configuring card...")
    req = {"req": "service.set"}
    req["product"] = "com.blues.brandon.raspberry-pi"
    req["mode"] = "continuous"
    rsp = send_request(req)

    print("Getting Status...")
    req = {"req": "service.status"}
    rsp = send_request(req)

    for i in range(10):
      print("Adding note...")
      req = {"req":"note.add"}
      req["body"] = {"foo": "bar"}
      rsp = send_request(req)
      time.sleep(2)


if __name__ == "__main__":
  main()