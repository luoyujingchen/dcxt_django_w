import datetime
import os
import time
from _sha1 import sha1

from django.db import models
from django.utils.text import get_valid_filename
from django.utils.translation import ugettext_lazy as _

from dcxt_django import settings
from multiuploader.utils import generate_safe_pk
import multiuploader.default_settings as DEFAULTS

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(null=True,blank=True)
    discount = models.FloatField(null=True,blank=True)# 请先检查discount_prices是否设置，discount_price存在的时候禁止设置discount
    weight = models.IntegerField(default=1)
    introduction = models.TextField(blank=True)


class BaseAttachment(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    ac_name = models.CharField(max_length=255)
    # ac_by = models.ForeignKey(to=Dish, on_delete=models.CASCADE)
    ac_upload_date = models.DateTimeField()

    @generate_safe_pk
    def generate_pk(self):
        return self

    def save(self, *args, **kwargs):
        if not self.upload_date:
            self.upload_date = datetime.datetime.now()

        if not self.pk:
            self.pk = self.generate_pk()

        super().save(*args, **kwargs)

class MultiuploaderFile(BaseAttachment):
    def _upload_to(instance, filename):
        upload_path = getattr(settings, 'MULTIUPLOADER_FILES_FOLDER', DEFAULTS.MULTIUPLOADER_FILES_FOLDER)

        if upload_path[-1] != '/':
            upload_path += '/'

        filename = get_valid_filename(os.path.basename(filename))
        filename, ext = os.path.splitext(filename)
        hash = sha1(str(time.time())).hexdigest()
        fullname = os.path.join(upload_path, "%s.%s%s" % (filename, hash, ext))

        return fullname

    file = models.FileField(upload_to=_upload_to, max_length=255)

    def save(self, *args, **kwargs):
        self.filename = os.path.basename(self.file.path)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('multiuploader file')
        verbose_name_plural = _('multiuploader files')