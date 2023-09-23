from django import template

register = template.Library()

@register.simple_tag
def replace(request, key, value):
    url_dict = request.GET.copy()
    print("=" * 30)
    print(url_dict)
    url_dict[key] = value
    print("=" * 30)
    print(url_dict.urlencode())

    return url_dict.urlencode()