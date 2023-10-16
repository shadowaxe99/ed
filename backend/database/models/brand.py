```python
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'brands'

    brand_id = Column(Integer, primary_key=True)
    name = Column(String)
    industry = Column(String)
    values = Column(JSON)

    def __init__(self, name, industry, values):
        self.name = name
        self.industry = industry
        self.values = values
```