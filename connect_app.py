from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import sys
from globalvar import *

MyRequest = None
newRequest = False



class RequestHandler_httpd(BaseHTTPRequestHandler):
    def do_GET(self):
        global newRequest, MyRequest, COUNT
        MyRequest = self.requestline
        MyRequest = MyRequest[5:int(len(MyRequest) - 9)]
        print(newRequest)
        newRequest = True
        print(newRequest)
        print("You received this request: {}".format(MyRequest))

        #upload file

        #send message 
        if MyRequest == "Get_Data":
            message_to_send = bytes("{}_{}_{}_{}_{}".format(glob_time, glob_temp, glob_bpm, glob_env_temp, glob_env_humid), "utf")
        else:
            message_to_send = bytes("hi", "utf")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", len(message_to_send))
        self.end_headers()
        self.wfile.write(message_to_send)
        return


if __name__ == '__main__':
    def other_arduino_function():
        global newRequest, MyRequest
        print("Listening to Arduino...")
        while True:
            if newRequest:
                print("my request: {}".format(MyRequest))
                newRequest = False
            # time.sleep(5)


    def run_server():
        print("Start Server")
        httpd.serve_forever()

    try:
        server_address_httpd = (sys.argv[1], 8080)
    except:
        server_address_httpd = ('192.168.0.106', 8080)
    httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)

    threads = []
    thread_server = threading.Thread(target=run_server)
    threads.append(thread_server)
    thread_arduino = threading.Thread(target=other_arduino_function)
    threads.append(thread_arduino)
    # thread.daemon = True
    for t in threads:
        t.start()
