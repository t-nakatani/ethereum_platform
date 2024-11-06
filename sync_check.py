import requests
import json

# Ethereumノードへのリクエストを設定
url = 'http://127.0.0.1:8545'
headers = {'Content-Type': 'application/json'}
data = json.dumps({
    "jsonrpc": "2.0",
    "method": "eth_syncing",
    "params": [],
    "id": 1
})

# POSTリクエストを送信
response = requests.post(url, headers=headers, data=data)

# レスポンスをJSON形式で取得
result = response.json().get('result', {})

# Hex値を10進数に変換して出力
if result:
    print("Current Block:", int(result['currentBlock'], 16))
    print("Highest Block:", int(result['highestBlock'], 16))
    print("Synced Accounts:", int(result['syncedAccounts'], 16))
    print("Synced Bytecodes:", int(result['syncedBytecodes'], 16))
    print("Synced Storage:", int(result['syncedStorage'], 16))
else:
    print("Not syncing or error in response")
