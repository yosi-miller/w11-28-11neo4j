from flask import Flask, request, jsonify,current_app
from database.init_db import init_neo4j
from server_bp import server_bp

app = Flask(__name__)

app.register_blueprint(server_bp)

with app.app_context():
    app.neo4j_driver = init_neo4j()


if __name__ == '__main__':
    app.run(debug=True)