from sqlalchemy import Column, String, Float, DateTime
from database import Base

class CVE(Base):
    __tablename__ = "cves"
    id = Column(String, primary_key=True, index=True)
    description = Column(String)
    published = Column(DateTime)
    modified = Column(DateTime)
    score = Column(Float)