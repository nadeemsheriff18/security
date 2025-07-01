import requests

def fetch_nvd_cves(results_per_page=10, start_index=0):
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    params = {
        "resultsPerPage": results_per_page,
        "startIndex": start_index
    }

    response = requests.get(url, params=params)

    # 🛡️ Check for HTTP errors
    if response.status_code != 200:
        print(f"❌ NVD error: {response.status_code}")
        print("Response text:", response.text[:300])
        return []

    try:
        data = response.json().get("vulnerabilities", [])
        result = []

        for item in data:
            cve = item.get("cve", {})
            result.append({
                "source": "NVD",
                "id": cve.get("id", ""),
                "description": cve.get("descriptions", [{}])[0].get("value", ""),
                "published": cve.get("published", "")
            })

        return result

    except Exception as e:
        print("❌ Error decoding NVD JSON:", e)
        print("Raw response:", response.text[:300])
        return []
