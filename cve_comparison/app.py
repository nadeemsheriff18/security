from nvd_fetcher import fetch_nvd_cves
from cnnvd_scraper import fetch_cnnvd
import pandas as pd
import os

os.makedirs("output", exist_ok=True)

nvd = fetch_nvd_cves(10)
cnnvd = fetch_cnnvd()

print(f"NVD CVEs fetched: {len(nvd)}")
print(f"CNNVD CVEs fetched: {len(cnnvd)}")

all_cves = nvd + cnnvd
df = pd.DataFrame(all_cves)
print("DataFrame preview:", df.head())

df.to_csv("output/cve_data.csv", index=False)
print("✅ All CVEs saved to output/cve_data.csv")
