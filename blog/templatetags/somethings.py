from django import template

register = template.Library()


@register.simple_tag
def mymedia(data):
    if data:
        return f'/media/{data}'
    return f'/media/blog/Image_not_available.png'
