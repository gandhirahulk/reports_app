from .constants import *
from . import models


def fetch_active_fields2(field_list):
    active_fields = {}

    no_status_fields = [STATUS, STATE_LIST]

    for field in field_list:
        if field != 'display_names':
            print(field)
            record = getattr(models, TEMPLATE_VARIABLE_TABLE).objects.get(field_name=field)
            sort_name = record.sort_column
            table_name = record.db_table_name
            if field in no_status_fields:
                active_fields[field] = getattr(models, table_name).objects.all()
            else:
                active_fields[field] = getattr(models, table_name).objects.filter(status=ACTIVE)
                    # .order_by(sort_name)

    return active_fields
