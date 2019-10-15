from flask import Flask, request,jsonify
from gevent.pywsgi import WSGIServer
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')
# Read the swagger.yml file to configure the endpoints
app.add_api('/home/app/function/swagger.yml', validate_responses=True)

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=False)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
