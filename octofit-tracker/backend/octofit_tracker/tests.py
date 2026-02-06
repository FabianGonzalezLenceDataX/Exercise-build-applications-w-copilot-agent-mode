from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(team), 'Test Team')
    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Test Team')
        self.assertEqual(str(user), 'Test User')
    def test_create_activity(self):
        activity = Activity.objects.create(user='test@example.com', activity='Run', duration=10)
        self.assertEqual(activity.activity, 'Run')
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user='test@example.com', points=5)
        self.assertEqual(lb.points, 5)
    def test_create_workout(self):
        workout = Workout.objects.create(user='test@example.com', workout='Push-ups', reps=20)
        self.assertEqual(workout.reps, 20)
