import os
import SimpleHTTPServer
import SocketServer
os.chdir("/mnt/sdcard/sl4a/scripts/web")
handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", 8000), handler)
httpd.serve_forever()