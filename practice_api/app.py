from flask import Flask, jsonify,render_template,request
import sqlite3
from db import init_db,load_data_from_json
import os

app=Flask(__name__)
DB="cves.db"

@app.before_first_request
def setup():
    if not os.path.exists(DB):
        init_db()
        load_data_from_json()

def query_db(query,args=(),one=False):
    conn=sqlite3.connect(DB)
    cursor=conn.cursor()
    cursor.execute(query,args)
    rows=cursor.fetchall()
    conn.close()
    return rows[0] if one else rows

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search',methods=['GET'])
def search():
    cve_id = request.args.get("cve_id")
    row = query_db("SELECT * FROM cves WHERE id = ?", [cve_id], one=True)

    if row:
        cve = {
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "severity": row[3],
            "published": row[4]
        }
    else:
        cve = None

    return render_template("cve.html", cve=cve)

@app.route('/cves/<cve_id>',methods=['GET'])
def search_by_id(cve_id):
    row=query_db('SELECT * FROM cves WHERE id=?',[cve_id],one=True)

    if row:
        return jsonify({
            "id": row[0],
            "title": row[1],
            "description": row[2],
            "severity": row[3],
            "published": row[4]
        })
    else:
        return jsonify({"error": "CVE not found"}), 404
if __name__=='__main__':
    app.run(debug=True)