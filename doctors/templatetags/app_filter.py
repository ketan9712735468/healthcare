from datetime import datetime
from django import template
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def age(value):
    now = datetime.now()
    print(value)
    try:
        difference = now.year - value.year

    except:
        return value

    # if difference <= timedelta(minutes=1):
    #     return 'just now'
    # difference = int(difference.strftime('%Y'))
    return difference
           # % {'time': timesince(value).split(', ')[0]}
