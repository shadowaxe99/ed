import requests
import unittest

from backend.user_profile_management.user import User
from backend.user_profile_management.preferences import Preferences
from backend.brand_database.brand import Brand
from backend.matching_algorithm.matching import Matching
from backend.partnership_idea_generator.idea_generator import IdeaGenerator
from backend.email_automation.email import Email
from backend.email_automation.response_tracker import ResponseTracker
from backend.pitch_deck_generator.deck_generator import DeckGenerator
from backend.analytics_dashboard.analytics import Analytics
from backend.security.security import Security

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.user = User()
        self.preferences = Preferences()
        self.brand = Brand()
        self.matching = Matching()
        self.idea_generator = IdeaGenerator()
        self.email = Email()
        self.response_tracker = ResponseTracker()
        self.deck_generator = DeckGenerator()
        self.analytics = Analytics()
        self.security = Security()

    def test_user_profile_management(self):
        response = requests.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.get_user(), response.json())

    def test_brand_database(self):
        response = requests.get('/api/brands/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.brand.get_brand(), response.json())

    def test_matching_algorithm(self):
        response = self.matching.match(self.user, self.brand)
        self.assertTrue(response)

    def test_partnership_idea_generator(self):
        response = self.idea_generator.generate_idea(self.user, self.brand)
        self.assertIsNotNone(response)

    def test_email_automation(self):
        response = self.email.send_email(self.user, self.brand)
        self.assertEqual(response.status_code, 200)

    def test_response_tracker(self):
        response = self.response_tracker.track_response(self.email)
        self.assertIsNotNone(response)

    def test_pitch_deck_generator(self):
        response = self.deck_generator.generate_deck(self.idea_generator)
        self.assertIsNotNone(response)

    def test_analytics_dashboard(self):
        response = self.analytics.get_metrics()
        self.assertIsNotNone(response)

    def test_security(self):
        response = self.security.check_security(self.user)
        self.assertTrue(response)

if __name__ == '__main__':
    unittest.main()