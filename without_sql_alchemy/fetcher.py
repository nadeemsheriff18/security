import requests

def fetch_cves(limit=15, start=0):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "resultsPerPage": limit,
        "startIndex": start
    }
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print("Error:", response.status_code)
        return []

    try:
        return response.json().get("vulnerabilities", [])
    except:
        print("Invalid JSON")
        return []
