from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User


class TestViews(TestCase):
    def test_url_nueva_solicitud(self):
        self.user_login()
        response = self.client.get('/solicitudes/nueva')
        self.assertEqual(response.status_code, 200)

    def test_nombre_url_nueva_solicitud(self):
        self.user_login()
        response = self.client.get(reverse('solicitudes:nueva'))
        self.assertEqual(response.status_code, 200)

    def test_template_nueva_solicitud(self):
        self.user_login()
        response = self.client.get('/solicitudes/nueva')
        self.assertTemplateUsed(response, 'solicitudes/solicitud_form.html')

    def user_login(self):
        usuario = User.objects.create_user(username='juca', password='juca123')
        self.client.login(username='juca', password='juca123')
        return usuario
