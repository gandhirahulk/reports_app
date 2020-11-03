# from .models import status
from report_app.models import status

# STATUS
ACTIVE = status.objects.get(status_name='active')
DEACTIVE = status.objects.get(status_name='inactive')

# VIEWS
MANAGE_EMPLOYEE_VIEW = 'Associate_app:manageemployee'
DASHBOARD_VIEW = 'Associate_app:dashboard'
LOGIN_VIEW = 'Associate_app:login'
ORGANIZATION_VIEW = 'Associate_app:organization'

ROLES_VIEW = 'Associate_app:roles'
ROLE_MAP_VIEW = 'Associate_app:rolemap'

GROUP_VIEW = 'Associate_app:groups'
GROUP_ASSIGN_VIEW = 'Associate_app:groupassign'
GROUP_REVOKE_VIEW = 'Associate_app:grouprevoke'

ATTENDANCE_RULE_VIEW = 'Associate_app:manage_attendance'
TEAM_ATTENDANCE_VIEW = 'Associate_app:team_attendance'
WORKFLOW_VIEW = 'Associate_app:workflow'
SHIFT_VIEW = 'Associate_app:manage_shift'
HOLIDAY_VIEW = 'Associate_app:manage_holiday'
HOLIDAY_RULE_VIEW = 'Associate_app:manage_holiday_rule'

# URLS
LEAVE_URL = 'settings/leave/'
ORGANIZATION_URL = 'settings/organization/'
ROLES_URL = 'settings/roles/'
GROUPS_URL = 'settings/groups/'
WORKFLOW_URL = 'settings/workflow/'
DATA_ACCESS_RIGHTS_URL = 'settings/data_access_rights/'
GENERAL_URL = 'settings/General/'

SHIFT_URL = 'settings/shift/'
RECRUITMENT_URL = 'settings/Recruitment/'
EMPLOYEE_POLICY_URL = 'settings/EmployeePolicy/'

ATTENDANCE_URL = 'dashboard/attendance/'

SETTINGS_ATTENDANCE_URL = 'settings/attendance/'
SETTINGS_HOLIDAY_URL = 'settings/holiday/'
SETTINGS_HOLIDAY_RULE_URL = 'settings/holiday_rule/'

TEAM_ATTENDANCE_URL = 'self_service/team/team_attendance/'
SELF_ATTENDANCE_URL = 'self_service/attendance/'
PAYROLL_URL = 'reports/payroll/'

TRANSFER_URL = 'workforce/transfer/'
SEPARATION_URL = 'workforce/separation/'
CONFIRMATION_URL = 'workforce/confirmation/'

MANAGE_EMPLOYEE_URL = 'workforce/manageemployee/'
EMPLOYEE_ADD_URL = 'workforce/manageemployee/add_new_employee/'
EMPLOYEE_IMPORT_URL = 'workforce/manageemployee/import_employees/'
CHECK_DUPLICATE_ID_URL = 'workforce/manageemployee/check_duplicate_eid/'

# HTML
TABLE_HTML = 'table.html'
CREATE_HTML = 'create.html'
EDIT_HTML = "edit.html"
VIEW_HTML = "view.html"

LOGIN_HTML = 'Associate_app/login.html'
DASHBOARD_HTML = 'Associate_app/dashboard/dashboard.html'
THEMES_HTML = 'Associate_app/themes.html'
RECRUITMENT_HTML = 'Associate_app/settings/recruitment/recruitment.html'
GENERAL_HTML = 'Associate_app/settings/general/general.html'
TRANSFER_HTML = 'Associate_app/workforce/transfer/transfer.html'
SEPARATION_HTML = 'Associate_app/workforce/separation/seperation.html'
CONFIRMATION_HTML = 'Associate_app/workforce/confirmation/confirmation.html'
LOGIN_REDIRECT_HTML = 'Associate_app/loginredirect.html'

WORKFLOW_HTML = 'Associate_app/settings/workflow/table.html'
WORKFLOW_EDIT_HTML = 'Associate_app/settings/workflow/edit.html'
WORKFLOW_ADD_HTML = 'Associate_app/settings/workflow/create.html'
WORKFLOW_MAP_HTML = 'Associate_app/settings/workflow/map.html'

DATA_ACCESS_RIGHTS_HTML = 'Associate_app/settings/data_access_rights/table.html'
DATA_ACCESS_RIGHTS_ADD_HTML = 'Associate_app/settings/data_access_rights/create.html'
DATA_ACCESS_RIGHTS_EDIT_HTML = 'Associate_app/settings/data_access_rights/edit.html'

ROLES_HTML = 'Associate_app/settings/roles/table.html'
ROLE_SETTING_MAP_EDIT_HTML = "Associate_app/settings/roles/edit.html"
ROLE_MAP_HTML = "Associate_app/settings/roles/rolemap.html"
ROLE_DATA_MAP_HTML = 'Associate_app/settings/roles/roledatamap.html'

GROUPS_HTML = 'Associate_app/settings/groups/table.html'
GROUP_ASSIGN_HTML = 'Associate_app/settings/groups/assign.html'
GROUP_EDIT_HTML = "Associate_app/settings/groups/edit.html"
GROUP_VIEW_HTML = "Associate_app/settings/groups/view.html"
GROUP_MAP_HTML = 'Associate_app/settings/groups/map.html'

ATTENDANCE_HTML = 'Associate_app/settings/attendance/take_attendance.html'
ATTENDANCE_SHIFT_HTML = 'Associate_app/settings/attendance/mappings/shift/shift_mapping.html'
ATTENDANCE_POLICY_HTML = 'Associate_app/settings/attendance/mappings/policy/policy_mapping.html'
ATTENDANCE_ORG_HTML = 'Associate_app/settings/attendance/mappings/org/org_mapping.html'
ATTENDANCE_OD_HTML = 'Associate_app/settings/attendance/mappings/od/od_mapping.html'


REPORTS_HTML = 'table.html'

MANAGE_ATTENDANCE_HTML = 'Associate_app/settings/attendance/table.html'

HOLIDAY_HTML = 'Associate_app/settings/holiday/table.html'
MAP_HOLIDAY_RULE_HTML = 'Associate_app/settings/holiday_rule/mapping/holiday.html'

HOLIDAY_RULE_HTML = 'Associate_app/settings/holiday_rule/table.html'
HOLIDAY_RULE_ORG_HTML = 'Associate_app/settings/holiday_rule/mapping/org.html'
EDIT_HOLIDAY_RULE_HTML = 'Associate_app/settings/holiday_rule/edit.html'

# SETTINGS/SHIFTS
SHIFT_TEMPLATE_PATH = 'Associate_app/settings/shift/'
SHIFT_HTML = SHIFT_TEMPLATE_PATH + TABLE_HTML
SHIFT_CREATE_HTML = SHIFT_TEMPLATE_PATH + CREATE_HTML
SHIFT_EDIT_HTML = SHIFT_TEMPLATE_PATH + EDIT_HTML

TEAM_ATTENDANCE_HTML = 'Associate_app/self_service/team/team_attendance/team_attendance.html'
SHOW_ATTENDANCE_HTML = 'Associate_app/self_service/team/team_attendance/emp_attendance_report.html'
SELF_ATTENDANCE_HTML = 'Associate_app/self_service/attendance/self_attendance_report.html'

# SETTINGS/ORGANIZATION
ORGANIZATION_TEMPLATE_PATH = 'Associate_app/settings/organization/'

ORGANIZATION_HTML = ORGANIZATION_TEMPLATE_PATH + 'organization.html'

EDIT_GENDER_HTML = ORGANIZATION_TEMPLATE_PATH + "gender/" + EDIT_HTML
EDIT_SUB_LOCATION_HTML = ORGANIZATION_TEMPLATE_PATH + "sub_location/" + EDIT_HTML
EDIT_LOCATION_HTML = ORGANIZATION_TEMPLATE_PATH + "location/" + EDIT_HTML
EDIT_STATE_HTML = ORGANIZATION_TEMPLATE_PATH + "state/" + EDIT_HTML
EDIT_REGION_HTML = ORGANIZATION_TEMPLATE_PATH + "region/" + EDIT_HTML
EDIT_DESIGNATION_HTML = ORGANIZATION_TEMPLATE_PATH + "designation/" + EDIT_HTML
EDIT_ROLE_HTML = ORGANIZATION_TEMPLATE_PATH + "role/" + EDIT_HTML
EDIT_SUB_FUNCTION_HTML = ORGANIZATION_TEMPLATE_PATH + "sub_function/" + EDIT_HTML
EDIT_FUNCTION_HTML = ORGANIZATION_TEMPLATE_PATH + "function/" + EDIT_HTML
EDIT_BUSINESS_HTML = ORGANIZATION_TEMPLATE_PATH + "business/" + EDIT_HTML
EDIT_VENDOR_HTML = ORGANIZATION_TEMPLATE_PATH + "vendor/" + EDIT_HTML
EDIT_COMPANY_HTML = ORGANIZATION_TEMPLATE_PATH + "company/" + EDIT_HTML
EDIT_TEAM_HTML = ORGANIZATION_TEMPLATE_PATH + "team/" + EDIT_HTML
EDIT_GROUP_HTML = ORGANIZATION_TEMPLATE_PATH + "group/" + EDIT_HTML


VIEW_GENDER_HTML = ORGANIZATION_TEMPLATE_PATH + "gender/" + VIEW_HTML
VIEW_SUB_LOCATION_HTML = ORGANIZATION_TEMPLATE_PATH + "sub_location/" + VIEW_HTML
VIEW_LOCATION_HTML = ORGANIZATION_TEMPLATE_PATH + "location/" + VIEW_HTML
VIEW_STATE_HTML = ORGANIZATION_TEMPLATE_PATH + "state/" + VIEW_HTML
VIEW_REGION_HTML = ORGANIZATION_TEMPLATE_PATH + "region/" + VIEW_HTML
VIEW_DESIGNATION_HTML = ORGANIZATION_TEMPLATE_PATH + "designation/" + VIEW_HTML
VIEW_ROLE_HTML = ORGANIZATION_TEMPLATE_PATH + "role/" + VIEW_HTML
VIEW_SUB_FUNCTION_HTML = ORGANIZATION_TEMPLATE_PATH + "sub_function/" + VIEW_HTML
VIEW_FUNCTION_HTML = ORGANIZATION_TEMPLATE_PATH + "function/" + VIEW_HTML
VIEW_BUSINESS_HTML = ORGANIZATION_TEMPLATE_PATH + "business/" + VIEW_HTML
VIEW_VENDOR_HTML = ORGANIZATION_TEMPLATE_PATH + "vendor/" + VIEW_HTML
VIEW_TEAM_HTML = ORGANIZATION_TEMPLATE_PATH + "team/" + VIEW_HTML
VIEW_GROUP_HTML = ORGANIZATION_TEMPLATE_PATH + "group/" + VIEW_HTML
VIEW_COMPANY_HTML = ORGANIZATION_TEMPLATE_PATH + "company/" + VIEW_HTML
COMPANY_MODAL = ORGANIZATION_TEMPLATE_PATH + 'company/' + 'view.html'

COMPANY_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "company/" + TABLE_HTML
SUB_LOCATION_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "sub_location/" + TABLE_HTML
LOCATION_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "location/" + TABLE_HTML
STATE_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "state/" + TABLE_HTML
REGION_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "region/" + TABLE_HTML
DESIGNATION_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "designation/" + TABLE_HTML
ROLE_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "role/" + TABLE_HTML
SUB_FUNCTION_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "sub_function/" + TABLE_HTML
FUNCTION_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "function/" + TABLE_HTML
BUSINESS_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "business/" + TABLE_HTML
TEAM_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "team/" + TABLE_HTML
GROUP_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "group/" + TABLE_HTML
VENDOR_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "vendor/" + TABLE_HTML
GENDER_TABLE_HTML = ORGANIZATION_TEMPLATE_PATH + "gender/" + TABLE_HTML


CREATE_COMPANY_HTML = ORGANIZATION_TEMPLATE_PATH + "company/" + CREATE_HTML
CREATE_SUB_LOCATION_HTML = ORGANIZATION_TEMPLATE_PATH + "sub_location/" + CREATE_HTML
CREATE_LOCATION_HTML = ORGANIZATION_TEMPLATE_PATH + "location/" + CREATE_HTML
CREATE_STATE_HTML = ORGANIZATION_TEMPLATE_PATH + "state/" + CREATE_HTML
CREATE_REGION_HTML = ORGANIZATION_TEMPLATE_PATH + "region/" + CREATE_HTML
CREATE_DESIGNATION_HTML = ORGANIZATION_TEMPLATE_PATH + "designation/" + CREATE_HTML
CREATE_ROLE_HTML = ORGANIZATION_TEMPLATE_PATH + "role/" + CREATE_HTML
CREATE_SUB_FUNCTION_HTML = ORGANIZATION_TEMPLATE_PATH + "sub_function/" + CREATE_HTML
CREATE_FUNCTION_HTML = ORGANIZATION_TEMPLATE_PATH + "function/" + CREATE_HTML
CREATE_BUSINESS_HTML = ORGANIZATION_TEMPLATE_PATH + "business/" + CREATE_HTML
CREATE_TEAM_HTML = ORGANIZATION_TEMPLATE_PATH + "team/" + CREATE_HTML
CREATE_GROUP_HTML = ORGANIZATION_TEMPLATE_PATH + "group/" + CREATE_HTML
CREATE_VENDOR_HTML = ORGANIZATION_TEMPLATE_PATH + "vendor/" + CREATE_HTML
CREATE_GENDER_HTML = ORGANIZATION_TEMPLATE_PATH + "gender/" + CREATE_HTML


# SETTINGS/WORKFORCE/MANAGE EMPLOYEE
MANAGE_EMPLOYEE_TEMPLATE_PATH = 'Associate_app/workforce/manage_employee/'
EMPLOYEE_POLICY_HTML = MANAGE_EMPLOYEE_TEMPLATE_PATH+'employeepolicy.html'
EMPLOYEE_IMPORT_HTML = MANAGE_EMPLOYEE_TEMPLATE_PATH+'import_employee/import_employee.html'
EMPLOYEE_DOCUMENTS_HTML = MANAGE_EMPLOYEE_TEMPLATE_PATH+'employeedocuments.html'
EMPLOYEE_HISTORY_HTML = MANAGE_EMPLOYEE_TEMPLATE_PATH+'employeehistory.html'
EMPLOYEE_PROFILE_HTML = MANAGE_EMPLOYEE_TEMPLATE_PATH+'employeeprofile.html'
EMPLOYEE_VIEW_HTML = MANAGE_EMPLOYEE_TEMPLATE_PATH+'view_employee/view_employee.html'
EMPLOYEE_ADD_HTML = MANAGE_EMPLOYEE_TEMPLATE_PATH+'add_employee/add_employee.html'
EMPLOYEE_MANAGE_HTML = MANAGE_EMPLOYEE_TEMPLATE_PATH+'manage_employee/manage_employee.html'

# DELETE MESSAGES
GENDER_DELETE_MESSAGE = "Gender Deleted Successfully"
SELF_SERVICE_DISABLED = "Self Service Disabled"

# SUCCESS MESSAGES
SELF_SERVICE_ENABLED = "Self Service Enabled"
CREATED_SUCCESSFULLY = " Created Successfully!"
ASSIGNED_SUCCESSFULLY = "  Assigned Successfully"
UNASSIGNED_SUCCESSFULLY = " Unassigned Successfully"
MAPPED_SUCCESSFULLY = " Mapped Successfully"
LOGGED_OUT_SUCCESSFULLY = "User Logged out Successfully"
LOGGED_IN_SUCCESSFULLY = "Login Successful"
UPDATED_SUCCESSFULLY = " Updated Successfully"
PASSWORD_SENT_SUCCESSFULLY = "Password has been sent to the registered email id and mobile number!"
SUCCESSFULLY_MARKED = 'successfully marked'

# ERROR MESSAGES
ERROR = "Error: "
DELETE_ERROR = " Referenced By Other Modules Cannot Delete"
UPDATE_ERROR = " Already Exist Cannot Update"
DUPLICATE_ROLE_MESSAGE = "Role Already Mapped"
ALREADY_EXIST = " Already Exist!"
NOT_ASSIGNED = " Not Assigned"
ALREADY_ASSIGNED_TO = " Already Assigned to "
INVALID_CREDENTIALS = "Invalid Credentials"
UID_NOT_FOUND = 'UID Not Found'
PLEASE_ENTER_UID = "Please Enter UID"
PLEASE_ENTER_PASSWORD = "Please Enter Password"
TRY_AGAIN = " and Try Again"
SPECIFY_EMP_CODE = 'Employee code needs to be specified'
NULL_EMP_CODE = 'null value provided for employee code'
NOT_DOWNLOADED_LOG = "Not Downloaded Log File"
DEPENDENCY_ERROR = " does not meet the dependency requirements"
FK_EXCEPTION = "Foreign key exception"
EMPLOYEE_CODE_ERROR = 'Employee code needs to be specified'
INVALID_VALUE = 'Invalid Value'
DIRECTORY_CREATION_FAILED = 'directory creation failed'
NOT_YET_PUNCHED = 'Not Yet Punched'
NOT_VALID = "Not Valid"
NA = 'NA'

# FK ID
FK_GENDER_ID_ID = 'gender_id_id'
FK_MEMBER_ID = 'fk_member_no_id'
FK_MEMBER_NO = 'fk_member_no'
EDUCATION_NUMBER = 'education_number'
EXP_NUMBER = 'exp_number'
FK_UID = 'fk_uid_id'
FK_SUB_LOCATION_ID = 'fk_sub_location_id'
NAME = 'name'
DESCRIPTION = 'description'

FK_COMPANY_ID = 'fk_company_id'
FK_VENDOR_ID = 'fk_vendor_id'
FK_BUSINESS_ID = 'fk_business_id'
FK_GROUP_ID = 'fk_group_id'
FK_TEAM_ID = 'fk_team_id'
FK_FUNCTION_ID = 'fk_function_id'
FK_SUB_FUNCTION_ID = 'fk_sub_function_id'
FK_ROLE_ID = 'fk_role_id'
FK_DESIGNATION_ID = 'fk_designation_id'
FK_REGION_ID = 'fk_region_id'
FK_STATE_ID = 'fk_state_id'
FK_LOCATION_ID = 'fk_location_id'

# FK
FK_FUNCTION = 'fk_function'
FK_SUB_FUNCTION = 'fk_sub_function'
FK_ROLE = 'fk_role'
FK_REGION = 'fk_region'
FK_LOCATION = 'fk_location'
FK_STATE = 'fk_state'
FK_GENDER_ID = 'gender_id'
FK_BUSINESS = 'fk_business'
FK_GROUP = 'fk_group'
FK_TEAM = 'fk_team'
FK_COMPANY = 'fk_company'
FK_DESIGNATION = 'fk_designation'
FK_SUB_LOCATION = 'fk_sub_location'
FK_VENDOR = 'fk_vendor'
# TABLE NAMES


# SETTINGS/SHIFT
SETTINGS_SHIFT_MAPPING_TABLE = 'settings_shift_mapping'
PK_SHIFT_CODE = 'pk_shift_code'
SHIFT_CODE = 'shift_code'
SHIFT_NAME = 'shift_name'
START_TIME = 'start_time'
END_TIME = 'end_time'
NIGHT_SHIFT = 'night_shift'
SINGLE_PUNCH = 'single_punch'
AUTO_PUNCH = 'auto_punch'
TOTAL_SHIFT_HOURS = 'total_shift_hours'
WEEK_MAPPING = 'week_mapping'
WEEK_NO = 'week_no'
FK_SHIFT_ID = 'fk_shift_id'
SHIFT_TABLE = 'settings_shift'
HOURS_AND = " hours and "
MINUTES = " minutes"
FK_ATTENDANCE_RULE = 'fk_attendance_rule'
FK_ATTENDANCE_RULE_ID = 'fk_attendance_rule_id'
CANCELLATION_ALLOWED = 'cancellation_allowed'
HALF_DAY_ALLOWED = 'half_day_allowed'

# SHIFT MAPPING
MONDAY_MAPPING = 'monday_mapping'
TUESDAY_MAPPING = 'tuesday_mapping'
WEDNESDAY_MAPPING = 'wednesday_mapping'
THURSDAY_MAPPING = 'thursday_mapping'
FRIDAY_MAPPING = 'friday_mapping'
SATURDAY_MAPPING = 'saturday_mapping'
SUNDAY_MAPPING = 'sunday_mapping'

MAPPING_TYPE_NAME = 'mapping_type_name'

# ATTENDANCE
UID = 'uid'
IN_TIME = 'in_time'
OUT_TIME = 'out_time'
TOTAL_HOURS = 'total_hours'
ATTENDANCE_DATE = 'attendance_date'
LATITUDE = 'latitude'
LONGITUDE = 'longitude'
RADIUS = 'radius'
ACCURACY = 'accuracy'
WEBSITE = 'website'
PHONE = 'phone'
IP_ADDRESS = 'ip_address'
MAC_ADDRESS = 'mac_address'
SOURCE = 'source'
SUB_SOURCE = 'sub_source'
HRMS = 'HRMS'
ATTENDANCE = 'attendance'
# TABLE
ATTENDANCE_RULE_TABLE = 'settings_attendance_rules'
ATTENDANCE_OD_MAPPING = 'settings_attendance_rules_od_mapping'

ATTENDANCE_RULE_NAME = 'attendance_rule_name'
ATTENDANCE_RULE_DESCRIPTION = 'attendance_rule_description'
ATTENDANCE_RULES = 'attendance_rules'

DATE = 'date'
TIME = 'time'

# TABLES - IMPORT_EMPLOYEE
EMP_CODE = 'emp_code'
LOG = 'log'
FK_IMPORT_CODE_ID = 'fk_import_code_id'
FK_RECORD_ID = 'fk_record_name_id'
NEW_VALUE = 'new_value'
OLD_VALUE = 'old_value'
NOT_PRESENT = 'Not Present'
FIELD_NAME = 'field_name'
EMPLOYEE_CODE = 'Employee Code'
PROCESSED_RECORDS = 'processed_records'
ERRONEOUS_RECORDS = 'erroneous_records'
TOTAL_RECORDS = 'total_records'
PROCESSED_SUCCESSFULLY = 'Processed Successfully'
DELETED_SUCCESSFULLY = 'Deleted Successfully'
UPDATE = "Update"
INSERT = "Insert"

BACKUP_RECORD = 'backup_record'
DB_HEADER_NAME = 'db_header_name'
EMPLOYEE_RECORD = 'employee_record'
DATABASE_HEADER = 'database_header'
COLUMN = 'column'
TABLE_NAME = 'table_name'
COLUMN_TO_SEARCH = 'column_to_search'
FOREIGN_KEY = 'foreign_key'
CHILD_TABLE = 'child_table'
GRANDCHILD_FK = 'grandchild_fk'
CHILD_FK = 'child_fk'
FIELD_FK = 'field_fk'
FILE_NAME = 'file_name'
FILE_EXTENSION = 'file_extension'
FILE_PATH = 'file_path'
UPLOADER_UID = 'uploader_uid'
TYPE = 'type'

FK_MODULE_ID_ID = 'fk_module_id_id'
FK_SECTION_ID_ID = 'fk_section_id_id'

FK_MODULE_ID = 'fk_module_id'
FK_SUB_MODULE_ID = 'fk_sub_module_id'

# TABLES - MODULE_SECTION_FIELD
EMPLOYEES_TABLE = 'employees'
COMPANY_TABLE = 'master_company'
BUSINESS_TABLE = 'master_business'
SETTINGS_ROLE_TABLE = 'mst_settings_role'
VENDOR_TABLE = 'master_vendor'
FUNCTION_TABLE = 'master_function'
GROUP_TABLE = 'master_group'
TEAM_TABLE = 'master_team'
SUB_FUNCTION_TABLE = 'master_sub_function'
DESIGNATION_TABLE = 'master_designation'
ROLE_TABLE = 'master_role'
REGION_TABLE = 'master_region'
STATE_TABLE = 'master_state'
LOCATION_TABLE = 'master_location'
SUB_LOCATION_TABLE = 'master_sub_location'
ATTENDANCE_TABLE = "attendance"

STATUS_TABLE = 'utl_status'
THEMES_TABLE = 'utl_themes'
GENDER_TABLE = 'master_gender'

# TABLE / ATTENDANCE
ATTENDANCE_ORG_MAPPING_TABLE = 'settings_attendance_rules_org_mapping'

# TABLE/IMPORT
IMPORT_BACKUP_TABLE = 'import_backup'
IMPORT_LOG_TABLE = 'import_log'

# TABLE/UTILITY
REASON_FOR_LEAVING_TABLE = 'utl_reason_for_leaving'
QUALIFICATION_TABLE = 'utl_qualification_type'
TEMPLATE_VARIABLE_TABLE = 'template_variables'
HIERARCHY_TABLE = 'utl_hierarchy'

FAMILY_MAPPING_TABLE = 'utl_family_mapping'
FAMILY_DETAIL_TABLE = 'mst_emp_family_details'
EXP_TABLE = "mst_emp_prev_exp"
EDUCATION_TABLE = "mst_emp_education_details"
DOCUMENT_TABLE = "mst_emp_document_info"
ADDRESS_TABLE = "mst_emp_address_details"

SELF_SERVICE_TABLE = 'mst_emp_self_service'
REPORTING_MANAGER_TABLE = 'mst_reporting_manager'

MODULE_SECTION_FIELD_TABLE = 'mst_module_section_field'
MODULE_SECTION_TABLE = 'mst_module_section'
MODULE_TABLE = 'mst_module'

GROUPS_TABLE = 'mst_settings_group'
GROUPS_USER_MAPPING_TABLE = 'mst_settings_group_user_mapping'
GROUPS_MAPPING_TABLE = 'mst_settings_group_mapping'

WEB_MAP_TABLE = 'mst_settings_web_map'
# WORKFLOW
WORKFLOW_ID = 'workflow_id'
WORKFLOW_TABLE = 'settings_workflow'
WORKFLOW_DETAILS_TABLE = 'settings_workflow_level_details'
WORKFLOW_ACCESS_MAPPING_TABLE = 'settings_workflow_access_mapping'
WORKFLOW_MODULE_TABLE = 'settings_workflow_module'
WORKFLOW_SUB_MODULE_TABLE = 'settings_workflow_sub_module'
WORKFLOW_LEVEL_NAME = 'workflow_level_name'
PERIOD = 'period'
AUTO_ACTION = 'auto_action'
PERIOD_TYPE = 'period_type'
AUTO_ACTION_NAME = 'auto_action_name'
PERIOD_TYPE_NAME = 'period_type_name'

ROLE_MAPPING_TABLE = 'mst_role_access_mapping'
SETTINGS_ROLE_MAPPING_TABLE = 'mst_settings_role_mapping'

DATA_ACCESS_MAPPING_TABLE = 'mst_data_access_mapping'

# MISC
TIMESTAMP = "%Y%m%d%H%M%S"
NOT_LOGIN = '/notlogin/'
POST_METHOD = "POST"
ENABLED = "Enabled"
DOUBLE_DASH = "--"
SINGLE_DASH = "_"
CSRF_TOKEN = 'csrfmiddlewaretoken'
USER = "user"
SELECT = "Select "
ON = 'on'
OFF = 'off'
BLANK = ''
SPACE = " "
UNDERSCORE = "_"

# ORGANIZATION CHILD
BUSINESS = "Business"
VENDOR = "Vendor"
SUB_FUNCTION = "Sub Function"
FUNCTION = "Function"
LOCATION = "Location"
ROLE = "Role"
COMPANY = "Company"
TEAM= "Team"
REGION = "Region"
SUB_LOCATION = "Sub Location"
STATE = "State"
DESIGNATION = "Designation"
STATE_S = 'state'
LOCATION_S = 'location'

GROUP = "Group"
GENDER = "Gender"

# IDENTITY
LOGGED_IN_USER = "logged in user"
ADMIN = 'admin'

# PATHS
# EXCEL_TO_CSV_PATH = "media/excel_to_csv/import_logs/"
MEDIA_PATH = "media/imported_files/"
IMPORTED_FILES_PATH = '\\media\\imported_files\\'
DOUBLE_BACKSLASH = '\\'

# EXTENSIONS
XLSX = '.xlsx'
XLS = '.xls'
CSV = '.csv'
CSV_NO_DOT = 'csv'
DOT = '.'
JPEG = '.jpeg'

# IMPORT EMPLOYEE
DELETE_CHEAT = '#delete#'
UTF_8_ENCODING = "utf-8-sig"

# table headers


# FRONT END TEMPLATE TAGS

# DISPLAY NAMES
EMPLOYEES = 'employees'

COMPANIES = 'companies'
BUSINESSES = 'businesses'
GROUPS = 'groups'
TEAMS = "teams"
SUB_LOCATIONS = 'sublocations'
LOCATIONS = 'locations'
# DBSTATES = 'states'
REGIONS = 'regions'
ROLES = 'roles'
DESIGNATIONS = 'designations'
SUB_FUNCTIONS = 'subfunctions'
FUNCTIONS = 'functions'
VENDORS = 'vendors'
GENDERS = 'genders'
ST_ROLES = 'strolelist'
THEMES = 'themes'
SKILL_TYPE = 'skill_type'
FK_SKILL_TYPE_ID = 'fk_skill_type_id'
STATES = 'states'
STATE_LIST = 'state_list'
MODULES = 'modules'
SECTIONS = 'sections'
FIELDS = 'fields'
DB_ORDERING = 'db_ordering'
MAPPED_MODULES = 'mapped_modules'

WORKFLOW = 'workflow'
HOLIDAY_RULE = 'holiday_rule'
SUBMODULES = 'submodules'
ROLE_LIST = 'role_list'
LEVEL_OPTIONS_LIST = 'level_options_list'
LEVEL_NUMBER = 'level_number'
FK_WORKFLOW = 'fk_workflow'
FK_WORKFLOW_ID = 'fk_workflow_id'

PERIOD_TYPES = 'period_types'
ACTIONS = 'actions'

# SETTINGS/SHIFTS
SHIFTS = 'shifts'

DISPLAY_NAMES = 'display_names'
DISPLAY_NAME = 'display_name'

ADDRESS = 'address'
DOCUMENTS = 'documents'
EDUCATION = 'education'
FAMILY = 'family'
EXPERIENCE = 'experience'
SELF_SERVICE = 'self_service'
REPORTING_MANAGER = 'reporting_manager'

WORKFLOW_DESCRIPTION = 'workflow_description'
WORKFLOW_NAME = 'workflow_name'
SEQUENCE_NUMBER = 'sequence_number'
INTIMATION = 'intimation'
STATUS = 'status'
STATUS_ID = 'status_id'

SELECTED_COMPANY = 'viewcompany'
SELECTED_VENDOR = 'viewvendor'
SELECTED_FUNCTION = 'viewfunction'
SELECTED_SUBFUNCTION = 'viewsubfunction'
SELECTED_ROLE = 'viewrole'
SELECTED_DESIGNATION = 'viewdesignation'
SELECTED_REGION = 'viewregion'
SELECTED_STATE = 'viewstate'
SELECTED_LOCATION = 'viewlocation'
SELECTED_SUBLOCATION = 'viewsublocation'
SELECTED_BUSINESS = 'viewbusiness'
SELECTED_GROUP = 'view_group'
SELECTED_TEAM = 'view_team'

SELECTED_GENDER = 'viewgender'


# TABLE_COLUMN_NAME
COMPANY_NAME = 'company_name'
VENDOR_NAME = 'vendor_name'
GENDER_NAME = 'gender_name'
SUB_LOCATION_NAME = 'sub_location_name'
LOCATION_NAME = 'location_name'
STATE_NAME = 'state_name'
REGION_NAME = 'region_name'
DESIGNATION_NAME = 'designation_name'
ROLE_NAME = 'role_name'
SUB_FUNCTION_NAME = 'sub_function_name'
FUNCTION_NAME = 'function_name'
GROUP_NAME = 'group_name'
TEAM_NAME = 'team_name'
BUSINESS_NAME = 'business'

CONTACT_PERSON = 'contact_person'
THEME_COLOR_ID = 'theme_color_id'
LOGIN_BACKGROUND = 'login_background'
EMAIL = 'email'
LOGO = 'logo'
PORT = 'port'
SERVER = 'server'
PASSWORD = 'password'

# IMPORT
SUCCESSFULLY = 'Successfully'
FIELD_NAME_TEXT = 'Field Name'
OLD_VALUE_TEXT = 'Old Value'
NEW_VALUE_TEXT = 'New Value'
LOG_TEXT = 'Log'
FIELD_NAME_FK = 'fk_record_name__field_name'
PK_RECORD_CODE = 'pk_record_code'
SHEET1 = 'sheet1'
SOLID = "solid"

# ON DUTY

# TEMPLATE_VARIABLE FIELDS
OD_TYPES = 'od_types'
DEDUCTION_FROM = 'deduction_from'
DEDUCTION_TYPE = 'deduction_type'
LEAVES = 'leaves'
ATTENDANCE_DATA_TYPE = 'attendance_date_type'
ROUND_OFF_VALUES = 'round_off_values'
HOLIDAY_TYPES = 'holiday_types'
HOLIDAYS = 'holidays'
HOLIDAY_RULES = 'holiday_rules'
REPORT_TYPES = 'report_types'
FREQUENCIES = 'frequencies'
DIMENSIONS = 'dimensions'
CITIES = 'cities'
SUB_TEAMS = 'sub_teams'

# SETTINGS/ATTENDANCE/VIEWS
RULE_ID = 'rule_id'
HALF_DAY = 'half_day'
CANCEL = 'cancel'

# SETTINGS/HOLIDAY/DB_UTILS
HOLIDAY_TABLE = 'settings_holiday'
HOLIDAY_RULE_TABLE = 'settings_holiday_rule'
HOLIDAY_RULE_ORG_TABLE = 'settings_holiday_rule_org'
HOLIDAY_NAME = 'holiday_name'
HOLIDAY_DATE = 'holiday_date'
YEAR = 'year'
FK_HOLIDAY_RULE = 'fk_holiday_rule'
FK_HOLIDAY_RULE_ID = 'fk_holiday_rule_id'

FK_HOLIDAY_TYPE = 'fk_holiday_type'
FK_HOLIDAY_TYPE_ID = 'fk_holiday_type_id'

HOLIDAY_TYPE = 'holiday_type'

# VIEW RECORD
VIEW_NAME = 'Name : '
VIEW_DESCRIPTION = 'Description : '
VIEW_CREATED_BY = 'Created By : '
VIEW_CREATED_AT = 'Created At : '
VIEW_MODIFIED_AT = 'Modified At : '
VIEW_MODIFIED_BY = 'Modified By : '

CREATED_BY = 'created_by'
CREATED_AT = 'created_date_time'
MODIFIED_AT = 'modified_date_time'
MODIFIED_BY = 'modified_by'
