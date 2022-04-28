from . import __version__ as app_version

app_name = "thearabgoals_theme"
app_title = "Thearabgoals Theme"
app_publisher = "GreyCube Technologies"
app_description = "Logo for thearablgoals.com"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/thearabgoals_theme/css/thearabgoals_theme.css"
# app_include_js = "/assets/thearabgoals_theme/js/thearabgoals_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/thearabgoals_theme/css/thearabgoals_theme.css"
# web_include_js = "/assets/thearabgoals_theme/js/thearabgoals_theme.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "thearabgoals_theme/public/scss/website"

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

website_context = {
    "splash_image": "/assets/thearabgoals_theme/images/arab_goals.png"
}
# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "thearabgoals_theme.install.before_install"
# after_install = "thearabgoals_theme.install.after_install"
after_install = "thearabgoals_theme.install.after_install"
# Uninstallation
# ------------

# before_uninstall = "thearabgoals_theme.uninstall.before_uninstall"
# after_uninstall = "thearabgoals_theme.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "thearabgoals_theme.notifications.get_notification_config"

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
# 		"thearabgoals_theme.tasks.all"
# 	],
# 	"daily": [
# 		"thearabgoals_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"thearabgoals_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"thearabgoals_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"thearabgoals_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "thearabgoals_theme.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "thearabgoals_theme.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "thearabgoals_theme.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"thearabgoals_theme.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
