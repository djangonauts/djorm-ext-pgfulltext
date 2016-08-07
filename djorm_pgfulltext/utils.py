import psycopg2

from django.conf import settings
from django.utils.text import force_text


def adapt(text):
    a = psycopg2.extensions.adapt(force_text(text))
    dbconfig = getattr(settings,"DATABASES", {'default': None})['default']
    if not dbconfig:
        raise "'default' DATABASES connection is required in settings.py for djorm_ext_pgfulltext."
    try:
        pgconn= psycopg2.connect(database=dbconfig['NAME'], user=dbconfig['USER'], password=dbconfig['PASSWORD'], host=dbconfig['HOST'], port = dbconfig['PORT'])
        a.prepare(pgconn)
    finally:
        pgconn.close()
    return a
