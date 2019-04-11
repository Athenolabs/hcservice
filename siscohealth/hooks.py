# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "siscohealth"
app_title = "Sisco Health"
app_publisher = "navdeepghai1@gmail.com"
app_description = "Healthcare Services"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "navdeepghai1@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = [
	"/assets/css/hcservice.min.css"
]
app_include_js = [
	"/assets/js/hcservice.min.js"
]

# include js, css files in header of web template
web_include_css = [
	"/assets/css/hcservice-web.min.css"
]
web_include_js = [
	"/assets/js/hcservice-web.min.js"
]


# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {
	"Patient" : "public/js/controllers/listview/patient_list.js"
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "hcservice.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "hcservice.install.before_install"
# after_install = "hcservice.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hcservice.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Patient Encounter": {
 		"validate": "siscohealth.controllers.base_controller.handle_doc_event",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hcservice.tasks.all"
# 	],
# 	"daily": [
# 		"hcservice.tasks.daily"
# 	],
# 	"hourly": [
# 		"hcservice.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hcservice.tasks.weekly"
# 	]
# 	"monthly": [
# 		"hcservice.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "hcservice.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hcservice.event.get_events"
# }
update_website_context = "siscohealth.website.website.get_context"
website_context = {
	"favicon":      "/assets/hcservice/images/logo/siscohealth-logo.png",
	"splash_image": "/assets/hcservice/images/logo/siscohealth-logo.png"
}
