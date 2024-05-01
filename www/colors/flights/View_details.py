import frappe
from datetime import datetime
from frappe.utils import format_date, format_duration

def get_context(context):
    context.no_cache = 1
    flight_name = frappe.form_dict.flight
    flight_fields = ["name", "airplane", "source_airport_code", "destination_airport_code", "date_of_departure", "time_of_departure", "duration"]
    flight_values = frappe.db.get_value("Airplane Flight", {"name": flight_name}, flight_fields, as_dict=True)
    
    if flight_values:
        formatted_date = format_date(flight_values['date_of_departure'], "d MMMM, YYYY")
        flight_values['formatted_date_of_departure'] = formatted_date
        
        formatted_duration = format_duration(flight_values['duration'])
        flight_values['formatted_duration'] = formatted_duration
        
        context.flights = [flight_values]
    else:
        context.flights = []
    
    return context