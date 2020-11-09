from django.db import models
from django.template.defaulttags import register

# from .. import models
import report_app
import report_app.models

from ..constants import STATUS, ACTIVE

...


@register.filter
def get_sub_field(table):
    query = getattr(report_app.models, table).objects.filter(**{STATUS: ACTIVE})
    id_to_fk_map = {}
    id_to_name_map = {}
    fk = ''

    for field in getattr(report_app.models, table).objects.filter(**{STATUS: ACTIVE}).first()._meta.concrete_fields:
        if isinstance(field, models.ForeignKey):
            if field.related_model._meta.db_table != 'report_app_status':
                fk = field.related_model._meta.db_table.replace('report_app_', '')

    if fk != '':
        for field in query:
            id_to_name_map[field.pk] = getattr(field, 'name')
            id_to_fk_map[field.pk] = getattr(field, str(fk + '_id'))

    if fk =='':
        for field in query:
            id_to_name_map[field.pk] = getattr(field, 'name')
            id_to_fk_map[field.pk] = getattr(field, 'name')

    query_dict = {'id_to_fk': id_to_fk_map, 'id_to_name': id_to_name_map}
    return query_dict
