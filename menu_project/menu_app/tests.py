from django.test import TestCase
from django.urls import reverse
from .models import MenuItem


class MenuTagTests(TestCase):
    def setUp(self):
        self.menu_item = MenuItem.objects.create(
            title='Test Menu', url='/test/', named_url='test_page')
        self.menu_name = 'main_menu'

    def test_draw_menu(self):
        response = self.client.get(reverse('test_page'))
        menu_html = response.context['menu_html']
        expected_html = '<ul><li class="active"><a href="/test/">Test Menu</a></li></ul>'
        self.assertHTMLEqual(menu_html, expected_html)

    def test_draw_menu(self):
        response = self.client.get(reverse('test_page'))
        menu_html = response.context['menu_html']
        expected_html = "<ul><li class='active'><a href='/test/'>Test Menu</a></li></ul>"
        self.assertEqual(menu_html.strip(), expected_html)
