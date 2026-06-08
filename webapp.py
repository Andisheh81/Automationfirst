import requests

api_url = "http://universities.hipolabs.com/search"

# FIX: Update the name to match the server's database spelling
query_parameters = {"country": "Turkiye"}

response = requests.get(api_url, params=query_parameters)

if response.status_code == 200:
    results = response.json() 
    
    # DEFENSIVE CHECK: Make sure the list is not empty!
    # len(results) counts how many items are in the list.
    if len(results) > 1:
        
        second_uni = results[1] 
        uni_name = second_uni['name']
        uni_websites_list = second_uni['web_pages']
        first_website = uni_websites_list[0]
        
        print(f"✅ University Name: {uni_name}")
        print(f"🌐 University Website: {first_website}")
        
    else:
        print("⚠️ Warning: The API returned an empty list or not enough results for that country.")
        
else:
    print(f"❌ Error connecting to the API. Status code: {response.status_code}")