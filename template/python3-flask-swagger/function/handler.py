import json
from flask import Blueprint, request

handler_blueprint = Blueprint('handle', __name__)

@handler_blueprint.route("/", defaults={"path": ""}, methods=["POST", "GET"])
def handle():
    
    result = json.loads(request.get_data(), encoding='utf-8')

    "magic_happends_here"

    return result