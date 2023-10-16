```python
import datetime
from backend.database.models.user import User
from backend.database.models.brand import Brand
from backend.security.security import GDPRCompliance

class LegalCompliance:
    def __init__(self):
        self.gdpr_compliance = GDPRCompliance()

    def quarterly_review(self):
        current_date = datetime.datetime.now()
        quarter_start = current_date - datetime.timedelta(days=90)

        users = User.query.filter(User.created_at >= quarter_start).all()
        brands = Brand.query.filter(Brand.created_at >= quarter_start).all()

        for user in users:
            self.gdpr_compliance.check_compliance(user)

        for brand in brands:
            self.gdpr_compliance.check_compliance(brand)

        return "Quarterly review completed successfully."

    def handle_compliance_issue(self, entity):
        # Placeholder for handling compliance issues
        pass

    def update_terms_of_service(self, new_terms):
        # Placeholder for updating terms of service
        pass

    def update_privacy_policy(self, new_policy):
        # Placeholder for updating privacy policy
        pass
```