from atexit import register
from django import template
from public.forms import ContactForm

register = template.Library()
@register.inclusion_tag("public/tags/form.html")
def contact_form():
    return {"contact_form": ContactForm()}