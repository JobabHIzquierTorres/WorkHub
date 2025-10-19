from django import template
from notices.models import Notice

register = template.Library()


@register.simple_tag
def get_notice_list():
    notices = Notice.objects.all()
    return notices
