import frappe


def execute():
	if frappe.db.exists("LMS Course", {"title": "A guide to Frappe Learning"}):
		frappe.db.set_value(
			"LMS Course",
			{"title": "A guide to Frappe Learning"},
			{
				"title": "A guide to Nayfaaro",
				"short_introduction": "Learn the basics of Nayfaaro and how to get started with your very first course.",
			},
		)

	if frappe.db.exists("LMS Quiz", {"title": "Do you know Frappe Learning?"}):
		frappe.db.set_value(
			"LMS Quiz",
			{"title": "Do you know Frappe Learning?"},
			"title",
			"Do you know Nayfaaro?",
		)
