from django import template
from django.core.cache import cache
from menu_app.models.menu import MenuItem
from typing import Any

register = template.Library()


def build_menu(menu_items: list[MenuItem], current_path: str, active_item: MenuItem = None) -> str:
    menu_html = "<ul>"

    for item in menu_items:
        active = "active" if current_path == item.url else ""
        if item == active_item:
            active = "active"
        menu_html += f"<li class='{active}'><a href='{item.url}'>{item.title}</a>"

        submenu_items = MenuItem.objects.filter(parent=item)
        if submenu_items:
            submenu_html = build_menu(submenu_items, current_path, active_item)
            menu_html += submenu_html

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

        cache.set(f'menu_{menu_name}', menu_html, 1)

    return menu_html
