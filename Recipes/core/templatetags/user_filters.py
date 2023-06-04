import urllib.request
from io import BytesIO

from django import template
from django.utils.safestring import mark_safe
from PIL import Image

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})


#@register.filter
#def image_resize(url, size):
#    image = Image.open(url)
#    image = image.resize(size)
#    return image





#@register.filter
#def image_resize(url):
#    size = (200, 250)
#    response = urllib.request.urlopen(url)
#    image_data = response.read()
#    image = Image.open(BytesIO(image_data))
#    image = image.resize(size)
#    output = BytesIO()
#    image.save(output, format='JPEG')
#    output.seek(0)
#    return output.getvalue()
#
#@register.filter
#def b64encode(data):
#    return base64.b64encode(data).decode('utf-8')



@register.filter
def image_resize(image_url, size):
    response = urllib.request.urlopen(image_url)
    image_data = response.read()
    image = Image.open(BytesIO(image_data))
    image = image.resize(size)
    output = BytesIO()
    image.save(output, format='JPEG')
    output.seek(0)
    return mark_safe(output.getvalue().decode('latin1'))