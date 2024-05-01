import frappe
from datetime import datetime

def get_context(context):
    context.no_cache = 1
    context.flights = [
        {
            **flight,
            'formatted_date': flight['date_of_departure'].strftime('%d %B %Y'),
            'formatted_duration': f"{int(flight['duration'] // (24 * 60 * 60))}d {(int(flight['duration'] // (60 * 60)) % 24)}h {int((flight['duration']//60) % 60)}m {int(flight['duration']%60)}s"
        }
        for flight in frappe.get_all("Airplane Flight", fields=["name", "airplane", "source_airport_code", "destination_airport_code", "date_of_departure", "time_of_departure", "duration"])
    ]
    return context