import requests
import json
import os

# MEXC API Endpoint (no authentication required)
url = "https://api.mexc.com/api/v3/capital/config/getall"

# Make the request
response = requests.get(url)
response.raise_for_status()  # Raise an error if API fails
data = response.json()

eth_tokens = []

for token in data:
    for network in token.get("networkList", []):
        if network.get("network", "").upper() == "ETH":
            eth_tokens.append({
                "symbol": token.get("coin"),
                "name": token.get("name"),
                "contract_address": network.get("contractAddress"),
                "network": network.get("network"),
                "withdraw_fee": network.get("withdrawFee"),
                "deposit_enable": network.get("depositEnable"),
                "withdraw_enable": network.get("withdrawEnable"),
            })

# Create /data directory if not exists
os.makedirs("data", exist_ok=True)

# Save output to JSON file
with open("data/mexc_eth_tokens.json", "w") as f:
    json.dump(eth_tokens, f, indent=2)

print(f"✅ Done! {len(eth_tokens)} Ethereum tokens saved to data/mexc_eth_tokens.json.")
