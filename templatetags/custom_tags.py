from django.contrib.admin.templatetags.admin_list import pagination
from django.contrib.admin.templatetags.base import InclusionAdminNode
from django.template import Library

register = Library()


@register.tag(name="custom_pagination")
def pagination_tag(parser, token):
    return InclusionAdminNode(
        parser,
        token,
        func=pagination,
        template_name="custom_pagination.html",
        takes_context=False,
    )