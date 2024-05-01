// Copyright (c) 2024, Krutika Tatte and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // Add a custom button to the form action bar
        frm.add_custom_button(('Assign Seat'), function() {
            // Show a dialog with an input field for entering the seat number
            new frappe.ui.Dialog({
                title: ('Enter Seat Number'),
                fields: [
                    {
                        label: ('Seat Number'),
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: true
                    }
                ],
                primary_action_label: ('Set'),
                primary_action(values) {
                    // Set the entered seat number to the 'Seat' field in the form
                    frm.set_value('seat', values.seat_number);
                    cur_dialog.hide();
                }
            }).show();
        }, __('Action'));
    }
});