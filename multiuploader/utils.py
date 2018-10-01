from _sha1 import sha1
from random import choice

from dcxt_django import settings


def generate_safe_pk(self):
    def wrapped(self):
        while 1:
            skey = getattr(settings, 'SECRET_KEY', 'asidasdas3sfvsanfja242aako;dfhdasd&asdasi&du7')
            pk = sha1('%s%s' % (skey, ''.join([choice('0123456789') for i in range(11)]))).hexdigest()

            try:
                self.__class__.objects.get(pk=pk)
            except:
                return pk

    return wrapped

#Getting files here
def format_file_extensions(extensions):
    return  ".(%s)$" % "|".join(extensions)