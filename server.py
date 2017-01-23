import os
import googlemaps
import json
from flask import Flask,jsonify,request,redirect,Response
from flask import render_template

API_KEY = 'AIzaSyCzpbgoECGhplawnFLBNgCVStWyMY30Ku8'

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    resp = Response("{'error':'404','description':'URL not found'}")
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp      

@app.route('/')
def index():
    return app.send_static_file('index.html')	

@app.route('/testapi/')
def testapi():
    val = request.args.get('q','nada')
    print val
    resp = Response("{'hello':'world','param':'%s'}" % val)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp      

port = os.getenv('PORT',5000)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port = int(port))

'''
try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()
'''

