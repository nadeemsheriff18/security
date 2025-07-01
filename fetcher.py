import requests

def fetch_cves(results_per_page=10, start_index=0):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "resultsPerPage": results_per_page,
        "startIndex": start_index
    }

    response = requests.get(url, params=params)

    # 🛡️ Check for HTTP errors
    if response.status_code != 200:
        print(f"Error: Received status {response.status_code}")
        print("Response text:", response.text[:300])  # print first 300 characters
        return []

    try:
        return response.json().get("vulnerabilities", [])
    except Exception as e:
        print("Error decoding JSON:", e)
        print("Raw response:", response.text[:300])
        return []
