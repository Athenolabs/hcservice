from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on transactions against this Patient. See timeline below for details'),
		'fieldname': 'patient_intake',
		'transactions': [
			{
				'label': _('Patient Encounters'),
				'items': ['Patient Encounter']
			},
			
			{
				'label': _('Patient Appointments'),
				'items': ['Patient Appointment']
			},
		]
	}
