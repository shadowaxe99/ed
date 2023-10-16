```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Partnership(Base):
    __tablename__ = 'partnerships'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    brand_id = Column(Integer, ForeignKey('brands.id'))
    partnership_idea = Column(String)
    status = Column(String)

    user = relationship("User", back_populates="partnerships")
    brand = relationship("Brand", back_populates="partnerships")

    def __init__(self, user_id, brand_id, partnership_idea, status):
        self.user_id = user_id
        self.brand_id = brand_id
        self.partnership_idea = partnership_idea
        self.status = status
```