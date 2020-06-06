import connect_app as ca
import get_pulse_temp as pulse
from http.server import HTTPServer
import argparse
import threading

def run_server():
    global httpd
    print("Start Server")
    httpd.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Webcam pulse detector.')
    parser.add_argument('--serial', default=None,
                        help='serial port destination for bpm data')
    parser.add_argument('--baud', default=None,
                        help='Baud rate for serial transmission')
    parser.add_argument('--udp', default=None,
                        help='udp address:port destination for bpm data')
    parser.add_argument('--subject', default='yph')
    parser.add_argument('--init_temp', type=float, default=36.5)
    parser.add_argument('--video', default="",
                        help='video name (only analyze one video)')
    parser.add_argument('--video_dir', default=None, help='directory name of all videos to be analyzed')

    parser.add_argument('--save_dir', default='data_pulse', help='directory to save the csv files')
    parser.add_argument('--BT', default=b'98:D3:71:F9:89:EC', type=bytes)
    parser.add_argument('--url', default=None, type=str,
                        help='IP Webcam url (ex: http://192.168.0.101:8080/video)')
    parser.add_argument('--server_address', default="172.20.10.9", type=str, help="the ip address of the computer running")

    args = parser.parse_args()


    server_address_httpd = (args.server_address, 8080)
    httpd = HTTPServer(server_address_httpd, ca.RequestHandler_httpd)

    threads = []
    thread_server = threading.Thread(target=run_server)
    threads.append(thread_server)
    thread_arduino = threading.Thread(target=pulse.get_pulse, args=[args])
    threads.append(thread_arduino)
    # thread.daemon = True
    for t in threads:
        t.start()




