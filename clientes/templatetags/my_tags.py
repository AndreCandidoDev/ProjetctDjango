from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag(name='current_time')
def current_time(format_string):
    return str(datetime.now().strftime(format_string))

# usage: {% your_tag_function 'function_parameters_values' as varible_name %}

