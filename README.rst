django-jsoneditor
=================

Provide Django integration for https://github.com/wjosdejong/jsoneditoronline

::
        JSON Editor Online
        http://jsoneditoronline.org

        JSON Editor Online is a tool to easily edit and format JSON online. 
        JSON is displayed in a clear, editable treeview and in formatted plain text.

Based on ``ad929bcfc07ff9285248f370c19c31e732ab3d1c`` of jsoneditoronline

Requirements
------------

https://github.com/derek-schaefer/django-json-field

(See ``reqs.txt``)

Installation
------------

Add ``jsoneditor`` to ``INSTALLED_APPS``:

::
        INSTALLED_APPS = (
        ...
        'jsoneditor',
        ...
        )

