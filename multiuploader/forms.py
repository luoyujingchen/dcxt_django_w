import json
import os
import re

from django import forms
from django.utils.safestring import mark_safe

from django.conf import settings

import multiuploader.default_settings as DEFAULTS
from multiuploader.utils import format_file_extensions


class MultiuploadWidget(forms.MultipleHiddenInput):
    def __init__(self,attrs={}):
        super().__init__(attrs)

    def render(self,name,value,*attrs):
        widget_ = super().render(name,value,attrs)
        output = '<div id="hidden_container" style="display:none;">%s</div>'% widget_
        return mark_safe(output)


class MultiuploaderField(forms.MultiValueField):
    widget = MultiuploadWidget

    def formfield(self,**kwargs):
        kwargs['widget'] = MultiuploadWidget
        return self.formfield(**kwargs)

    def validate(self, value):
        super().validate(value)

    def clean(self, value):
        super().clean(value)

    def compress(self, data_list):
        if data_list:
            return data_list
        return None


class MultiuploadForm(forms.Form):
    file = forms.FileField()

    def __init__(self,*args,**kwargs):
        multiuploader_settings = getattr(settings, "MULTIUPLOADER_FORMS_SETTINGS", DEFAULTS.MULTIUPLOADER_FORMS_SETTINGS)
        form_type = kwargs.pop("form_type","default")

        options = {
            'maxFileSize':multiuploader_settings[form_type]["MAX_FILE_SIZE"],
            'acceptFileTypes': format_file_extensions(multiuploader_settings[form_type]["FILE_TYPES"]),
            'maxNumberOfFiles': multiuploader_settings[form_type]["MAX_FILE_NUMBER"],
            'allowedContentTypes': map(str.lower, multiuploader_settings[form_type]["CONTENT_TYPES"]),
            'autoUpload': multiuploader_settings[form_type]["AUTO_UPLOAD"]
        }

        self._options = options
        self.options = json.dumps(options)

        super().__init__(*args, **kwargs)

        self.fields["file"].widget = forms.FileInput(attrs = {'multiple':True})

    def clean_file(self):
        content = self.cleaned_data[u'file']

        filename_extension = os.path.splitext(content.name)

        if re.match(self._options['acceptFileTypes'], filename_extension, flags=re.I) is None:
            raise forms.ValidationError('acceptFileTypes')

        content_type = magic.from_buffer(content.read(1024), mime=True)

        if content_type.lower() in self._options['allowedContentTypes']:
            if content._size > self._options['maxFileSize']:
                raise forms.ValidationError("maxFileSize")
        else:
            raise forms.ValidationError("acceptFileTypes")

        return content


class MultiuploaderMultiDeleteForm(forms.Form):
    id = MultiuploaderField()