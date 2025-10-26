import json, sqlite3
)


conn = sqlite3.connect(DB, check_same_thread=False)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
id TEXT PRIMARY KEY,
timestamp TEXT,
account_id TEXT,
amount REAL,
currency TEXT,
merchant TEXT,
location TEXT,
card_present INTEGER,
channel TEXT,
raw_json TEXT)''')
conn.commit()


recent = {}
loc_history = {}


while True:
for msg in consumer:
tx = msg.value
cur.execute('INSERT OR REPLACE INTO transactions VALUES (?,?,?,?,?,?,?,?,?,?)', (
tx['transaction_id'], tx['timestamp'], tx['account_id'], tx['amount'],
tx['currency'], tx['merchant'], tx['location'], int(tx['card_present']),
tx['channel'], json.dumps(tx)))
conn.commit()


alerts = []
t = datetime.fromisoformat(tx['timestamp'])


# Regras simples
if tx['amount'] >= 10000:
alerts.append('Valor alto')


# Rápidas
acc = tx['account_id']
lst = recent.get(acc, [])
lst = [x for x in lst if x > t - timedelta(seconds=10)]
lst.append(t)
recent[acc] = lst
if len(lst) > 3:
alerts.append('Muitas transações rápidas')


# Localização
last = loc_history.get(acc)
if last and last[0] != tx['location'] and (t - last[1]) < timedelta(minutes=5):
alerts.append('Mudança rápida de localização')
loc_history[acc] = (tx['location'], t)


# Canal
if tx['channel'] == 'WEB' and tx['card_present']:
alerts.append('Canal incompatível')


if alerts:
print(f"⚠️ FRAUDE: {tx['transaction_id']} -> {', '.join(alerts)}")
else:
print(f"OK: {tx['transaction_id']} valor={tx['amount']}")
