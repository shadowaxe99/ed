```python
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Email(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('users.id'))
    receiver_id = Column(Integer, ForeignKey('brands.id'))
    subject = Column(String(255))
    body = Column(String(5000))
    sent_at = Column(DateTime)
    status = Column(String(50))

    sender = relationship('User', back_populates='sent_emails')
    receiver = relationship('Brand', back_populates='received_emails')

    def __init__(self, sender_id, receiver_id, subject, body, sent_at, status):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.subject = subject
        self.body = body
        self.sent_at = sent_at
        self.status = status
```