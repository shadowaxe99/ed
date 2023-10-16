```python
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Analytics(Base):
    __tablename__ = 'analytics'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    brand_id = Column(Integer)
    partnership_id = Column(Integer)
    email_id = Column(Integer)
    event = Column(String)
    timestamp = Column(DateTime)
    value = Column(Float)

    def __init__(self, user_id, brand_id, partnership_id, email_id, event, timestamp, value):
        self.user_id = user_id
        self.brand_id = brand_id
        self.partnership_id = partnership_id
        self.email_id = email_id
        self.event = event
        self.timestamp = timestamp
        self.value = value
```