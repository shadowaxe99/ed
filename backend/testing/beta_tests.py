import pytest
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

def test_beta_users():
    users = User.get_all()
    assert len(users) == 100, "Number of beta users should be 100"

def test_beta_brands():
    brands = Brand.get_all()
    assert len(brands) == 20, "Number of beta brands should be 20"

def test_matching_algorithm():
    for user in User.get_all():
        preferences = Preferences.get_by_user_id(user.id)
        matches = Matching.get_matches(user.id, preferences)
        assert matches, "Matching algorithm should return at least one match for each user"

def test_partnership_idea_generation():
    for user in User.get_all():
        ideas = IdeaGenerator.get_ideas(user.id)
        assert ideas, "Partnership Idea Generator should return at least one idea for each user"

def test_email_automation():
    for user in User.get_all():
        email = Email.get_by_user_id(user.id)
        assert email, "Email Automation should have sent at least one email for each user"

def test_response_tracking():
    for user in User.get_all():
        responses = ResponseTracker.get_by_user_id(user.id)
        assert responses, "Response Tracker should have recorded at least one response for each user"

def test_pitch_deck_generation():
    for user in User.get_all():
        deck = DeckGenerator.get_by_user_id(user.id)
        assert deck, "Pitch Deck Generator should have created at least one pitch deck for each user"

def test_analytics_dashboard():
    analytics = Analytics.get_all()
    assert analytics, "Analytics Dashboard should have recorded some data"

def test_security_measures():
    for user in User.get_all():
        is_secure = Security.check_user_security(user.id)
        assert is_secure, "Security measures should be in place for each user"

if __name__ == "__main__":
    pytest.main()