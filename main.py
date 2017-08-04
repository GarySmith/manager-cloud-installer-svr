from manager_cloud_installer_svr import server
from manager_cloud_installer_svr import socketio
from flask import Flask
import logging
import optparse
logging.basicConfig(level=logging.DEBUG)

LOG = logging.getLogger(__name__)
app = Flask(__name__)
app.register_blueprint(server.bp)

if __name__ == "__main__":

    default_host="127.0.0.1"
    default_port="5000"

    # Set up the command-line options
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host",
                      help="Hostname of the Flask app " + \
                           "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port",
                      help="Port for the Flask app " + \
                           "[default %s]" % default_port,
                      default=default_port)

    # Two options useful for debugging purposes, but
    # a bit dangerous so not exposed in the help message.
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=optparse.SUPPRESS_HELP)

    options, _ = parser.parse_args()

    # If the user selects the profiling option, then we need
    # to do a little extra setup

    socketio.init_app(app)
    socketio.run(app,
            host=options.host,
            port=int(options.port),
            use_reloader=True)
