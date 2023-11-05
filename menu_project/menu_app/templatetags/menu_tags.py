from django import template
from django.core.cache import cache
from menu_app.models.menu import MenuItem
from typing import Any

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context: dict[str, Any], menu_name: str) -> str:
    request = context['request']

    menu_html = cache.get(f'menu_{menu_name}')

    if menu_html is None:
        menu_items = MenuItem.objects.filter(parent__isnull=True)

        current_path = request.path_info

        menu_html = "<ul>"
        for item in menu_items:
            active = "active" if current_path == item.url else ""
            menu_html += f"<li class='{active}'><a href='{item.url}'>{item.title}</a></li>"
        menu_html += "</ul>"

        cache.set(f'menu_{menu_name}', menu_html, 3600)

    return menu_html
