from . import __version__ as app_version

app_name = "isppme"
app_title = "ISPPME"
app_publisher = "Percival Rapha"
app_description = "ISPPME Elearning & School Management System"
app_icon = "fa fa-graduation-cap"
app_color = "blue"
app_email = "percival@yate.co.zw"
app_license = "MIT"

required_apps = ['erpnext']

fixtures = [
    # Education
    "Course",
    
    # Core
    "Custom Field",
    "Client Script",
    "Property Setter",
    
    # Settings
    "System Settings",
    "Education Settings",
    "Website Settings",
    
    # Website
    "Color",
    "Website Theme",
    "Web Page",
]

app_logo_url = '/assets/isppme/images/isppme-logo-cropped.png'

brand_html = '<div><img src="/assets/isppme/images/isppme-logo-cropped.png"> TennisMart</div>'

website_context = {
    "favicon": "/assets/isppme/images/isppme-favicon.png",
    "splash_image": "/assets/isppme/images/isppme-logo-cropped.png",
    "brand_html": '<div><img src="/assets/isppme/images/isppme-logo-cropped.png" style=""></div>'
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/isppme/css/desk.css"
# app_include_js = "/assets/isppme/js/isppme.js"

# include js, css files in header of web template
web_include_css = "/assets/isppme/css/web.css"
# web_include_js = "/assets/isppme/js/isppme.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "isppme/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "isppme.utils.jinja_methods",
# 	"filters": "isppme.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "isppme.install.before_install"
# after_install = "isppme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "isppme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"isppme.tasks.all"
# 	],
# 	"daily": [
# 		"isppme.tasks.daily"
# 	],
# 	"hourly": [
# 		"isppme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"isppme.tasks.weekly"
# 	],
# 	"monthly": [
# 		"isppme.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "isppme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "isppme.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "isppme.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"isppme.auth.validate"
# ]
