"""
main

This snippet is executed just once for the machine.
But it creates a thread that keeps listening 'forever' for requests until it is quit. 
It means it is just a spark for the system which is actually built through the boostrap process.
"""

from wsgiref.simple_server import make_server
from framework.bootstrap import bootstrap

httpd = make_server('localhost', 8000, bootstrap)
print("Serving on port 8000 bitch...")
httpd.serve_forever()