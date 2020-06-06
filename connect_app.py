from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import sys
import numpy as np

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
            try:
                data_body = np.load("body_data.npy").astype(np.float)
                time = data_body[0]
                bpm = data_body[1]
                temp = data_body[2]

                data_env = np.load("env_data.npy").astype(np.float)
                env_temp = data_env[0]
                env_humid = data_env[1]

                message_to_send = bytes("{:.1f}_{:.1f}_{:.1f}_{:.1f}_{:.1f}".format(time, temp, bpm, env_temp, env_humid), "utf")
                print(message_to_send)
            except Exception as e:
                print(e)
                message_to_send = bytes("No Data", "utf")
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
