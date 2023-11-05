from django import template
from django.core.cache import cache
from menu_app.models.menu import MenuItem
from typing import Any

register = template.Library()


def build_menu(menu_items: list[MenuItem], current_path: str) -> str:

    menu_html = "<ul>"

    for item in menu_items:
        active = "active" if current_path == item.url else ""
        menu_html += f"<li class='{active}'><a href='{item.url}'>{item.title}</a>"
        submenu_items = MenuItem.objects.filter(parent=item)
        if submenu_items:
            menu_html += build_menu(submenu_items, current_path)
        menu_html += "</li>"
    menu_html += "</ul>"

    return menu_html


@register.simple_tag(takes_context=True)
def draw_menu(context: dict[str, Any], menu_name: str) -> str:
    request = context['request']

    menu_html = cache.get(f'menu_{menu_name}')

    if menu_html is None:
        root_menu_items = MenuItem.objects.filter(parent__isnull=True)
        current_path = request.path_info

        menu_html = build_menu(root_menu_items, current_path)

        cache.set(f'menu_{menu_name}', menu_html, 3600)

    return menu_html
