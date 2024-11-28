class TransactionRepository:
    def __init__(self, driver):
        self.driver = driver

    def create_transaction(self, transaction_data):
        with self.driver.session() as session:
            query = """
            MERGE (source:Device {account_id: $source_id, name: $source_name, brand: $source_brand, model: $source_model})
            MERGE (target:Device {account_id: $target_id, name: $target_name, brand: $target_brand, model: $target_model})
            CREATE (source)-[t:TRANSACTION {
                transaction_id: $transaction_id,
                method: $method,
                bluetooth_version: $bluetooth_version,
                signal_strength_dbm: $signal_strength_dbm,
                distance_meters: $distance_meters,
                duration_seconds: $duration_seconds,
                timestamp: datetime($timestamp)
            }]->(target)
            RETURN t.transaction_id as transaction_id
            """

            result = session.run(query, {
                'source_id': transaction_data["devices"][0]['id'],
                'source_name': transaction_data["devices"][0]['name'],
                'source_brand': transaction_data["devices"][0]['brand'],
                'source_model': transaction_data["devices"][0]['model'],

                'target_id': transaction_data["devices"][1]['id'],
                'target_name': transaction_data["devices"][1]['name'],
                'target_brand': transaction_data["devices"][1]['brand'],
                'target_model': transaction_data["devices"][1]['model'],

                # the transaction id is generated by the uuid library
                'transaction_id': f'{transaction_data["interaction"]["from_device"]}{transaction_data["interaction"]["to_device"]}',
                'method': transaction_data['interaction']['method'],
                'bluetooth_version': transaction_data['interaction']['bluetooth_version'],
                'signal_strength_dbm': transaction_data['interaction']['signal_strength_dbm'],
                'distance_meters': transaction_data['interaction']['distance_meters'],
                'duration_seconds': transaction_data['interaction']['duration_seconds'],
                'timestamp': transaction_data['interaction']['timestamp']
            })
            return result.single()['transaction_id']

    def find_devices_bluetooth_connected(self):
        with self.driver.session() as session:
            query = """
                MATCH (start:Device)
                MATCH (end:Device)
                WHERE start <> end
                MATCH path = shortestPath((start)-[:TRANSACTION*]->(end))
                WHERE ALL(r IN relationships(path) WHERE r.method = 'Bluetooth')
                WITH path, length(path) as pathLength
                ORDER BY pathLength DESC
                LIMIT 1
                RETURN length(path)
                """
            result = session.run(query)
            return result.data()

    def find_devices_connected_by_signal(self):
        with self.driver.session() as session:
            query = """
                MATCH (start:Device)
                MATCH (end:Device)
                WHERE start <> end
                MATCH path = shortestPath((start)-[:TRANSACTION*]->(end))
                WHERE ALL(r IN relationships(path) WHERE r.signal_strength_dbm >= -60)
                WITH path, length(path) as pathLength
                ORDER BY pathLength DESC
                RETURN path
                """
            result = session.run(query)
            return result.data()

    def find_devices_connected_by_id(self, device_id):
        with self.driver.session() as session:
            query = """

                """
            result = session.run(query, {'device_id': device_id})
            return result.data()

    def find_two_devices_connected(self, device_id_1, device_id_2):
        with self.driver.session() as session:
            query = """

                """
            result = session.run(query, {'device_id_1': device_id_1, 'device_id_2': device_id_2})
            return result.data()

    def find_most_recent_interaction(self, device_id):
        with self.driver.session() as session:
            query = """

                """
            result = session.run(query, {'device_id': device_id})
            return result.data()