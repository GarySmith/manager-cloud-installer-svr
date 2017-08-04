from flask import Blueprint, request, jsonify, Response, make_response
import pbr.version
import requests
import time

bp = Blueprint('server', __name__)

ARDANA_SERVER="http://localhost:5000/"


@bp.route("/<path:url>", methods=['GET','POST','PUT','DELETE'])
def root(url):

    # TODO: Add logic to handle specific URL that should *not* be
    # routed to the ARDANA_SERVER

    url = ARDANA_SERVER + url

    req = requests.Request(method=request.method, url=url,
            headers=request.headers, data=request.data)

    resp = requests.Session().send(req.prepare())

    return (resp.text, resp.status_code, resp.headers.items())
