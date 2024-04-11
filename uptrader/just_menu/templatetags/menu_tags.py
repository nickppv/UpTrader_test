from django import template
from ..models import Country

register = template.Library()


@register.inclusion_tag("just_menu/inclusion_tags/menu.html")
def draw_menu(country=None, brand=None):
    all_objects = Country.objects.all()
    context = {
        'all_objects': all_objects,
        'country': country,
        'brand': brand,
    }
    if country:
        cnt = Country.objects.get(country=country).pk
        open_country = Country.objects.filter(pk__lte=cnt)
        close_country = Country.objects.filter(pk__gt=cnt)
        context['open_country'] = open_country
        context['close_country'] = close_country
    return context
