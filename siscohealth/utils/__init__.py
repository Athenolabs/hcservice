'''
	Developer Navdeep
	Email navdeepghai1@gmail.com
'''

import frappe
from frappe import _, msgprint, throw
from frappe.utils import cstr, getdate, nowdate
import dateutil

def get_age(date_data):
	res = ""
	if date_data:
		born = getdate(date_data)
		age = dateutil.relativedelta.relativedelta(getdate(), born)
		res = cstr(age.years) + " year(s) " + cstr(age.months) + \
					" month(s) " + cstr(age.days) + " day(s)"
	return res
