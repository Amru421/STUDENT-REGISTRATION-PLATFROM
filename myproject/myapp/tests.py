from django.test import TestCase

from .models import Project


class ProjectPagesTests(TestCase):
    def test_student_registration_page_renders(self):
        response = self.client.get('/student_register/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student registration')
        self.assertContains(response, 'name="password1"')
        self.assertContains(response, 'name="password2"')

    def test_student_registration_creates_account(self):
        from django.contrib.auth import get_user_model

        response = self.client.post(
            '/student_register/',
            {
                'username': 'new-student',
                'password1': 'Xy!84qLm#2026',
                'password2': 'Xy!84qLm#2026',
            },
        )

        self.assertRedirects(response, '/student_login/')
        student = get_user_model().objects.get(username='new-student')
        self.assertTrue(student.check_password('Xy!84qLm#2026'))

    def test_student_login_page_renders(self):
        response = self.client.get('/student_login/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student login')
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="password"')

    def test_student_can_log_in(self):
        from django.contrib.auth import get_user_model

        user = get_user_model().objects.create_user(
            username='student',
            password='test-password-123',
        )

        response = self.client.post(
            '/student_login/',
            {'username': user.username, 'password': 'test-password-123'},
        )

        self.assertRedirects(response, '/')
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_homepage_shows_empty_state(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No projects registered yet.')

    def test_project_registration_saves_and_redirects(self):
        response = self.client.post(
            '/projects_register/',
            {
                'topic': 'Portfolio site',
                'languages_used': 'Python',
                'duration': 5,
            },
        )

        self.assertRedirects(response, '/')
        self.assertTrue(Project.objects.filter(topic='Portfolio site').exists())

    def test_invalid_registration_renders_form_errors(self):
        response = self.client.post(
            '/projects_register/',
            {
                'topic': 'Portfolio site',
                'languages_used': 'Python',
                'duration': 'not a number',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter a whole number.')
