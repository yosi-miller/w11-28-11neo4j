import logging
from flask import Flask, request, jsonify,current_app
from database.init_db import init_neo4j
from database.neo4j_service import TransactionRepository

app = Flask(__name__)

@app.route('/api/phone_tracker', methods=['POST'])
def phone_tracker():
    data = request.json
    try:
        repo = TransactionRepository(current_app.neo4j_driver)
        transaction_id = repo.create_transaction(data)

        return jsonify({
            'status': 'success',
            'transaction_id': transaction_id
        }), 201

    except Exception as e:
        print(f'Error in POST /api/v1/transaction: {str(e)}')
        logging.error(f'Error in POST /api/v1/transaction: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500

@app.route('/api/bluetooth_connected', methods=['GET'])
def get_devices_bluetooth_connected():
    try:
        repo = TransactionRepository(current_app.neo4j_driver)
        devices = repo.find_devices_bluetooth_connected()
        return jsonify(devices), 200
    except Exception as e:
        print(f'Error in GET /api/v1/transaction: {str(e)}')
        logging.error(f'Error in GET /api/v1/transaction: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500

with app.app_context():
    app.neo4j_driver = init_neo4j()


if __name__ == '__main__':
    app.run(debug=True)