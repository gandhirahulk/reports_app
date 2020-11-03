# from .models import status
from report_app.models import status

# STATUS
ACTIVE = status.objects.get(status_name='active')
IN_ACTIVE = status.objects.get(status_name='inactive')


# DISPLAY NAMES
STATUS = 'status'
EMPLOYEES = 'employees'
TEAMS = "teams"
LOCATIONS = 'locations'
REGIONS = 'regions'
CTC_SLABS = 'ctc_slabs'
EXIT_TYPES = 'exit_types'
AGES = 'ages'
EMP_TYPES = 'emp_types'
TENURES = 'tenures'
ENTITIES = 'entities'
DESIGNATIONS = 'designations'
FUNCTIONS = 'functions'
VENDORS = 'vendors'
GENDERS = 'genders'
REPORT_TYPES = 'report_types'
FREQUENCIES='frequencies'
DIMENSIONS='dimensions'
CITIES='cities'
SUB_TEAMS='sub_teams'
POST_METHOD = "POST"

STATES = 'states'
STATE_LIST = 'state_list'
NOT_LOGIN = '/notlogin/'
TEMPLATE_VARIABLE_TABLE = 'template_variables'

# HTML TEMPLATES
REPORTS_HTML = 'table.html'

