import requests

api_url = "http://universities.hipolabs.com/search"
query_parameters = {"country": "Turkiye"}

# 1. Open the safety cage
try:
    print("📡 Attempting to connect to the network...")
    response = requests.get(api_url, params=query_parameters, timeout=5) # Timeout stops it from waiting forever
    
    # If the code gets past the line above without a network crash, we proceed normally:
    if response.status_code == 200:
        results = response.json()
        
        if len(results) > 0:
            print(f"\n✅ Connection Stable. Printing {len(results[:10])} results:")
            for uni in results[:10]:
                name = uni['name']
                website = uni['web_pages'][0]
                print(f"🏫 {name} -> {website}")
        else:
            print("⚠️ API worked, but returned 0 results.")
    else:
        print(f"❌ Server rejected us. Status code: {response.status_code}")

# 2. Catch the specific network crash error if the internet fails
except requests.exceptions.RequestException as error_message:
    print("\n🚨 [NETWORK CRITICAL ERROR] 🚨")
    print("Could not connect to the internet or the server is completely down.")
    print(f"Details for debugging: {error_message}")