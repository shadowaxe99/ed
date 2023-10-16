```python
from sklearn.ensemble import RandomForestClassifier
from backend.database.models.user import User
from backend.database.models.brand import Brand

class MatchingAlgorithm:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def predict_match(self, user_preferences, brand_attributes):
        prediction = self.model.predict([user_preferences + brand_attributes])
        return prediction

    def get_user_preferences(self, user_id):
        user = User.query.get(user_id)
        return user.preferences

    def get_brand_attributes(self, brand_id):
        brand = Brand.query.get(brand_id)
        return brand.values

    def match_influencer_brand(self, user_id, brand_id):
        user_preferences = self.get_user_preferences(user_id)
        brand_attributes = self.get_brand_attributes(brand_id)
        match_score = self.predict_match(user_preferences, brand_attributes)
        return match_score
```