import logging
from flask import Blueprint
from flask import request, jsonify, current_app
from database.neo4j_service import TransactionRepository

server_bp = Blueprint('server_bp', __name__)

@server_bp.route('/api/phone_tracker', methods=['POST'])
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

@server_bp.route('/api/bluetooth_connected', methods=['GET'])
def get_devices_bluetooth_connected():
    try:
        repo = TransactionRepository(current_app.neo4j_driver)
        devices = repo.find_devices_bluetooth_connected()
        return jsonify(devices), 200
    except Exception as e:
        print(f'Error in GET /api/v1/transaction: {str(e)}')
        logging.error(f'Error in GET /api/v1/transaction: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500

# Expose flask’s endpoint for finding all devices connected to each other with a signal strength stronger than -60.
@server_bp.route('/api/devices_connected_by_signal', methods=['GET'])
def get_devices_connected_by_signal():
    try:
        repo = TransactionRepository(current_app.neo4j_driver)
        devices = repo.find_devices_connected_by_signal()
        return jsonify(devices), 200
    except Exception as e:
        print(f'Error in GET /api/v1/transaction: {str(e)}')
        logging.error(f'Error in GET /api/v1/transaction: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500

@server_bp.route('/api/devices_connected/<device_id>', methods=['GET'])
def get_devices_connected(device_id):
    try:
        repo = TransactionRepository(current_app.neo4j_driver)
        print(device_id)
        devices = repo.find_devices_connected_by_id(device_id)
        return jsonify(devices), 200
    except Exception as e:
        print(f'Error in GET /api/v1/transaction: {str(e)}')
        logging.error(f'Error in GET /api/v1/transaction: {str(e)}')
        return jsonify({'error': 'internal server error'}), 500

# @server_bp.route('/api/two_devices_connected/<device_id_1>/<device_id_2>', methods=['GET'])
# def get_two_devices_connected(device_id_1, device_id_2):
#     try:
#         repo = TransactionRepository(current_app.neo4j_driver)
#         devices = repo.find_two_devices_connected(device_id_1, device_id_2)
#         return jsonify(devices), 200
#     except Exception as e:
#         print(f'Error in GET /api/v1/transaction: {str(e)}')
#         logging.error(f'Error in GET /api/v1/transaction: {str(e)}')
#         return jsonify({'error': 'internal server error'}), 500
#
# @server_bp.route('/api/most_recent_interaction/<device_id>', methods=['GET'])
# def get_most_recent_interaction(device_id):
#     try:
#         repo = TransactionRepository(current_app.neo4j_driver)
#         devices = repo.find_most_recent_interaction(device_id)
#         return jsonify(devices), 200
#     except Exception as e:
#         print(f'Error in GET /api/v1/transaction: {str(e)}')
#         logging.error(f'Error in GET /api/v1/transaction: {str(e)}')
#         return jsonify({'error': 'internal server error'}), 500