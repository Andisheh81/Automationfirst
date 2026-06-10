import requests

api="https://jsonplaceholder.typicode.com/posts"

# This is the data we want to send to the server.
# We format it as a standard Python dictionary.
data = {
    "title": "Automating the Web with Python",
    "body": "This is a carefully written test report using a POST request.",
    "userId": 1
}

try:
    print("📤 Sending data to the server...")
    # We send the request. 'json=new_post_data' automatically converts
    # our Python dictionary into an internet-safe JSON string.
    response = requests.post(api, json=data, timeout=5)
    if response.status_code == 201:
        print("✅ Success! The server accepted our data and created the resource.")
        
        # Let's see what the server sent back to confirm receipt
        server_confirmation = response.json()
        print("\n--- Server Confirmation Receipt ---")
        print(server_confirmation)
        
    else:
        print(f"❌ Server rejected our data. Status code: {response.status_code}")

except requests.exceptions.RequestException as error:
    print(f"🚨 Network error occurred: {error}")