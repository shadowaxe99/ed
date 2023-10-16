```python
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password_hash = Column(String)
    preferences = Column(JSON)

    def __init__(self, username, email, password_hash, preferences):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.preferences = preferences
```