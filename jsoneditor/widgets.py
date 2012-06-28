# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from django.template.loader import render_to_string

from django.utils.safestring import mark_safe

from django import forms

class JSONEditor(forms.Textarea):
    class Media:
        css = {
            'all': ('css/jsoneditor.css',),
        }
        js = ('js/jsoneditor-min.js', 'js/interface.js')

    def render(self, name, value, attrs=None, **kwargs):
        rendered = super(JSONEditor, self).render(name, value, attrs=attrs, **kwargs)

        field_id = attrs['id']

        context = {
            'field_id': field_id,
        }

        return rendered +  mark_safe(render_to_string(
            'jsoneditor/jsoneditor_widget.html', context
        ))


# EOF

