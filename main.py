'''
Created on May 16, 2017

@author: hossam
'''
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi

PORT_NUMBER = 8080
 
#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
     
   
    #Handler for the POST requests
    def do_POST(self):
        if self.path=="/send":
            form = cgi.FieldStorage(
                fp=self.rfile, 
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
            })
            uploaded_file = form.getvalue("uploadedfile")
            
            #print "Your name is: %s" % form["uploadedfile"].file.read()
            print (self.client_address[0])
            filePath = self.client_address[0]+".mp3"
            if uploaded_file:
             with open(filePath, "wb") as fh:
                 fh.write(form["uploadedfile"].file.read())

            self.send_response(200)
            self.end_headers()
           
            return            
             
             
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER
     
    #Wait forever for incoming htto requests
    server.serve_forever()
 
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()


