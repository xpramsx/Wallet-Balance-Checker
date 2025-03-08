# Wallet Balance Checker
# Language: Python
# Description: Checks the balance of a crypto wallet (ETH, BSC, BTC)

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEYS = {
    "ethereum": os.getenv("ETHERSCAN_API_KEY"),
    "bsc": os.getenv("BSCSCAN_API_KEY"),
    "bitcoin": os.getenv("BLOCKCYPHER_API_KEY")
}

API_URLS = {
    "ethereum": "https://api.etherscan.io/api?module=account&action=balance&address={}&apikey=" + API_KEYS["ethereum"],
    "bsc": "https://api.bscscan.com/api?module=account&action=balance&address={}&apikey=" + API_KEYS["bsc"],
    "bitcoin": "https://api.blockcypher.com/v1/btc/main/addrs/{}/balance"
}

def get_wallet_balance(network, address):
    if network not in API_URLS:
        return "Unsupported network"
    
    url = API_URLS[network].format(address)
    response = requests.get(url)
    data = response.json()
    
    if network == "bitcoin":
        balance = data.get("balance", 0) / 1e8  # Convert satoshi to BTC
    else:
        balance = int(data.get("result", 0)) / 1e18  # Convert wei to ETH/BSC
    
    return f"Balance for {address} on {network.upper()}: {balance}"

if __name__ == "__main__":
    network = input("Enter network (ethereum/bsc/bitcoin): ").lower()
    address = input("Enter wallet address: ")
    print(get_wallet_balance(network, address))
