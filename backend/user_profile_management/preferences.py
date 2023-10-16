```python
from backend.database.models.user import User
from sqlalchemy.orm import Session

def get_preferences(user_id: int, db: Session):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        return None
    return user.preferences

def update_preferences(user_id: int, new_preferences: dict, db: Session):
    user = db.query(User).filter(User.user_id == user_id).first()
    if user is None:
        return None
    user.preferences = new_preferences
    db.commit()
    return user.preferences
```