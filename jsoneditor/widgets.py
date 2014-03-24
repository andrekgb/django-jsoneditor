# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.template.loader import render_to_string

from django.utils.safestring import mark_safe

from django.conf import settings

from django import forms

class JSONEditor(forms.widgets.Widget):
    class Media:
        css = {
            'all': ('jsoneditor.css',),
        }
        js = ('jsoneditor.js',)

    def render(self, name, value, attrs=None, **kwargs):
        rendered = super(JSONEditor, self).render(name, value, attrs=attrs, **kwargs)

        field_id = attrs['id']
        field = field_id.split('_', 1)[1]

        context = {
            'field_id': field_id,
            'field': field,
            'STATIC_URL': settings.STATIC_URL,
        }

        pre_html = mark_safe(render_to_string('jsoneditor/jsoneditor_pre.html', context))
        widget_html = mark_safe(render_to_string('jsoneditor/jsoneditor_widget.html', context))
        post_html = mark_safe(render_to_string('jsoneditor/jsoneditor_post.html', context))

        return pre_html + rendered + widget_html + post_html


# EOF

