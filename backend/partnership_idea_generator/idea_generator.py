```python
import random
from backend.database.models.user import User
from backend.database.models.brand import Brand

class IdeaGenerator:
    def __init__(self):
        self.user = User()
        self.brand = Brand()

    def generate_ideas(self, user_id):
        user_preferences = self.user.get_preferences(user_id)
        matched_brands = self.brand.get_matched_brands(user_preferences)
        partnership_ideas = self.create_partnership_ideas(matched_brands)
        return partnership_ideas

    def create_partnership_ideas(self, matched_brands):
        ideas = []
        for brand in matched_brands:
            idea = self.generate_idea(brand)
            ideas.append(idea)
        return ideas

    def generate_idea(self, brand):
        idea_templates = [
            f"Collaborate with {brand['name']} for a product giveaway",
            f"Host a live event with {brand['name']}",
            f"Create a co-branded product line with {brand['name']}",
            f"Start a social media campaign with {brand['name']}"
        ]
        return random.choice(idea_templates)
```