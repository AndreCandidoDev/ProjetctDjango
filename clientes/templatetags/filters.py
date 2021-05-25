from django import template

register = template.Library()
# usage: {{view_variable or first_parameter|filter_function:second_parameter}}


@register.filter(name='my_filter')
def my_filter(data):
    return str(data)+'-'+'change by filter and kill the fags'


@register.filter(name='arredonda')
def arredonda(value, casas):
    return round(value, casas)
# {{1245.55|arredonda:4}} ---- exemple
