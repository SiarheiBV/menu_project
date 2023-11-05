from django.template.loader import get_template
from menu_app.templatetags import draw_menu
from django.http import HttpRequest, HttpResponse


def menu_view(request: HttpRequest, menu_name: str) -> HttpResponse:
    menu_html = draw_menu({'request': request}, 'main_menu')

    context = {
        'menu_html': menu_html,
    }

    print(context)
    template = get_template('menu_template.html')
    rendered_content = template.render(context)
    return HttpResponse(rendered_content)
