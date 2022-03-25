import django.shortcuts


# Create your views here.
def index(request):
    context_dict = {'text': 'hello mtf', 'number': '10'}
    return django.shortcuts.render(request, 'basic_app/index.html', context_dict)


def other(request):
    return django.shortcuts.render(request, 'basic_app/other.html')


def relative(request):
    return django.shortcuts.render(request, 'basic_app/relative_url_templates.html')
