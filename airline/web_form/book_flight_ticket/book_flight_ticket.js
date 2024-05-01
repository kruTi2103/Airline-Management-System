frappe.ready(function() {
    var randomPrice = Math.floor(Math.random() * (20000 - 10000 + 1)) + 10000;
    frappe.web_form.set_value(["flight_price"], [randomPrice]);
});