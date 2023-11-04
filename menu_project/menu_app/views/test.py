from django.http import HttpResponse, HttpRequest
from django.template.loader import get_template
from menu_app.templatetags.menu_tags import draw_menu


def test_view(request: HttpRequest) -> HttpResponse:
    menu_html = draw_menu({'request': request}, 'main_menu')
    context = {
        'menu_html': menu_html,
    }
    template = get_template('test_template.html')
    rendered_content = template.render(context)
    return HttpResponse(rendered_content)
