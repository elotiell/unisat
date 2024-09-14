import json
from bitcoinlib.keys import HDKey

def load_wallets(wallet_file):
    with open(wallet_file, 'r') as f:
        wallets = json.load(f)
    
   
    for wallet in wallets:
        private_key = wallet.get("private_key")
        if private_key:
           key = HDKey().import_key(private_key)
wallet['address'] = key.address()  
    return wallets

def save_wallets(wallet_file, wallets_data):
    with open(wallet_file, 'w') as f:
        json.dump(wallets_data, f)


if __name__ == "__main__":
    wallets = load_wallets('wallets.json')
    print(wallets)
