from flask import Flask, jsonify, request, render_template
from db import init_db, get_db
from fetcher import fetch_cves
from datetime import datetime

app = Flask(__name__)
init_db()  # create table if not exists

def insert_cve(conn, cve):
    cur = conn.cursor()
    try:
        cve_id = cve["cve"]["id"]
        desc = cve["cve"]["descriptions"][0]["value"]
        published = cve["cve"]["published"]
        modified = cve["cve"]["lastModified"]

        score = None
        try:
            score = cve["cve"]["metrics"]["cvssMetricV3"][0]["cvssData"]["baseScore"]
        except:
            pass

        cur.execute("""
            INSERT OR REPLACE INTO cves (id, description, published, modified, score)
            VALUES (?, ?, ?, ?, ?)
        """, (cve_id, desc, published, modified, score))

    except Exception as e:
        print("Insert error:", e)

@app.route('/')
def home():
    return render_template("index.html")
    

@app.route("/fetch")
def fetch_and_store():
    conn = get_db()
    cves = fetch_cves()
    for cve in cves:
        insert_cve(conn, cve)
    conn.commit()
    conn.close()
    return jsonify({"stored": len(cves)})

@app.route("/search", methods=["GET"])
def search():
    year = request.args.get("year")
    if not year:
        return "Please enter a year", 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, description, published, modified, score 
        FROM cves 
        WHERE published LIKE ?
    """, (f"{year}-%",))
    
    rows = cur.fetchall()
    conn.close()

    result = [{
        "id": r[0],
        "description": r[1],
        "published": r[2],
        "modified": r[3],
        "score": r[4]
    } for r in rows]

    return render_template("index.html", results=result, year=year)

@app.route("/cves/list")
def list_cves():
    conn = get_db()
    cur = conn.cursor()
    page = int(request.args.get("page", 1))
    limit = 10
    offset = (page - 1) * limit

    
    cur.execute("SELECT id, description, published, modified, score FROM cves LIMIT ? OFFSET ?", (limit, offset))
    rows = cur.fetchall()

    cur.execute("SELECT COUNT(*) FROM cves")
    total = cur.fetchone()[0]

    conn.close()

    result = [{
        "id": r[0],
        "description": r[1],
        "published": r[2],
        "modified": r[3],
        "score": r[4]
    } for r in rows]

    return render_template("cves.html",results=result,page=page,total=total,limit=limit)

if __name__ == "__main__":
    app.run(debug=True)
