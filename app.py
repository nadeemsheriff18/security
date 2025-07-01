from flask import Flask,request,jsonify
from database import SessionLocal, engine
from models import Base, CVE
from fetcher import fetch_cves
from crud import save_cve

app=Flask(__name__)
Base.metadata.create_all(bind=engine)

@app.route("/fetch",methods=['GET'])
def fetch_and_store():
    db=SessionLocal()
    cves=fetch_cves()
    for cve in cves:
        save_cve(db,cve)
    #print(jsonify({'fetched':len(cves)}))
    return jsonify({'fetched':len(cves)})

@app.route('/cves/list',methods=['GET'])
def list_cves():
    db=SessionLocal()
    cves=db.query(CVE).limit(10).all()
    return jsonify([
        {
            "id": cve.id,
            "description": cve.description,
            "published": cve.published.isoformat(),
            "modified": cve.modified.isoformat(),
            "score": cve.score
        } for cve in cves
    ])

@app.route('/cves/<string:cve_id>',methods=["GET"])
def get_cve_by_id(cve_id):
    db=SessionLocal()
    cve=db.query(CVE).filter(CVE.id==cve_id).first()
    if not cve:
        return jsonify({
            "error": "CVE not found"
        })
    return jsonify({
 "id": cve.id,
        "description": cve.description,
        "published": cve.published.isoformat(),
        "modified": cve.modified.isoformat(),
        "score": cve.score
    })
if __name__=='__main__':
    app.run(debug=True)