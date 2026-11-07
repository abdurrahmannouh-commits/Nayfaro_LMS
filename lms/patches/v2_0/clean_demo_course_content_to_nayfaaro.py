import frappe


def execute():
	"""Update all existing demo course details, lessons, reviews, and tags in the database to Nayfaaro."""
	frappe.db.sql(
		"""
		UPDATE `tabLMS Course`
		SET tags = REPLACE(tags, 'Frappe', 'Nayfaaro'),
		    description = REPLACE(
		        REPLACE(description, 'Frappe Learning', 'Nayfaaro'),
		        'https://docs.frappe.io/learning',
		        '/lms'
		    )
		WHERE title LIKE '%A guide to%'
		   OR description LIKE '%Frappe Learning%'
		   OR tags LIKE '%Frappe%'
		"""
	)

	frappe.db.sql(
		"""
		UPDATE `tabCourse Lesson`
		SET title = REPLACE(title, 'Frappe Learning', 'Nayfaaro')
		WHERE title LIKE '%Frappe Learning%'
		"""
	)

	frappe.db.sql(
		"""
		UPDATE `tabCourse Review`
		SET review = REPLACE(review, 'Frappe Learning', 'Nayfaaro')
		WHERE review LIKE '%Frappe Learning%'
		"""
	)

	frappe.db.sql(
		"""
		UPDATE `tabLMS Question`
		SET question = REPLACE(question, 'Frappe Learning', 'Nayfaaro')
		WHERE question LIKE '%Frappe Learning%'
		"""
	)
