django-jsoneditor
=================

Provide Django integration for https://github.com/wjosdejong/jsoneditoronline

        JSON Editor Online
        http://jsoneditoronline.org

        JSON Editor Online is a tool to easily edit and format JSON online.
        JSON is displayed in a clear, editable treeview and in formatted plain text.

Includes versin 2.3.6 of jsoneditor as a git submodule.

Requirements
------------

https://github.com/derek-schaefer/django-json-field
https://github.com/josdejong/jsoneditor

(See ``requirements.txt``)

Installation
------------

Add ``jsoneditor`` to ``INSTALLED_APPS``:

        INSTALLED_APPS = (
        ...
        'jsoneditor',
        ...
        )

