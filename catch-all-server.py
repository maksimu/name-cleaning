__author__ = 'maustino'

import BaseHTTPServer


class HTTPHandlerOne(BaseHTTPServer.BaseHTTPRequestHandler):


    def do_GET(self): self.wfile.write("<html>"
                                       ""
                                       "<body>"
                                       "<h1>This server was relocated.</h1>"
                                       "<p>Please update your bookmarks to <a href=\"http://10.80.59.83:8080/ui/fms\"'><b>http://10.80.59.83:8080/ui/fms</b></a>"
                                       "</body>"
                                       "</html>")



def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=BaseHTTPServer.BaseHTTPRequestHandler):
    server_address = ('', 8000)
    print 'Starting server, use <Ctrl-C> to stop'
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run(handler_class=HTTPHandlerOne)
