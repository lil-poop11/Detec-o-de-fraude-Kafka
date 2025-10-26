import json, time, uuid, random
from datetime import datetime, timezone
from kafka import KafkaProducer


BROKER = 'localhost:9092'
TOPIC = 'transactions'
producer = KafkaProducer(bootstrap_servers=[BROKER], value_serializer=lambda v: json.dumps(v).encode('utf-8'))


accounts = [f'acc-{i:04d}' for i in range(1, 51)]
merchants = ['Loja A', 'Loja B', 'Loja C', 'Supermercado X']
channels = ['POS', 'WEB', 'MOBILE']
locations = ['Fortaleza,CE','Juazeiro do Norte,CE','São Paulo,SP']


while True:
tx = {
'transaction_id': str(uuid.uuid4()),
'timestamp': datetime.now(timezone.utc).isoformat(),
'account_id': random.choice(accounts),
'amount': round(random.uniform(1, 20000), 2),
'currency': 'BRL',
'merchant': random.choice(merchants),
'location': random.choice(locations),
'card_present': random.choice([True, False]),
'channel': random.choice(channels)
}
producer.send(TOPIC, tx)
producer.flush()
print(f"Enviada transação: {tx['transaction_id']} valor={tx['amount']}")
time.sleep(3)
