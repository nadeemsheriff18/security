from datetime import datetime
from models import CVE
def save_cve(db, cve):
    cve_id = cve["cve"]["id"]
    desc = cve["cve"]["descriptions"][0]["value"]
    
    # ✅ Convert ISO 8601 strings to datetime objects
    published = datetime.fromisoformat(cve["cve"]["published"])
    modified = datetime.fromisoformat(cve["cve"]["lastModified"])

    try:
        score = cve["cve"]["metrics"]["cvssMetricV3"][0]["cvssData"]["baseScore"]
    except:
        score = None

    db_cve = CVE(
        id=cve_id,
        description=desc,
        published=published,  # ✅ datetime object
        modified=modified,    # ✅ datetime object
        score=score
    )

    db.merge(db_cve)
    db.commit()
