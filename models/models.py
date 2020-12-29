from odoo import models, fields


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "OpenAcademy Sessions"

    name = fields.Char(required=True)
    instructor_name = fields.Char()
    basic_knowledge = fields.Char()
    category = fields.Selection([('programming_lang','Programming Language'), ('designing','Designing')])
    start_date = fields.Date()
    end_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

class Instructor(models.Model):
	_name = 'openacademy.instructor'
	_description = "OpenAcademy Instructor"

	instructor_name = fields.Char()
	instructor_id = fields.Integer(required=True)
	instructor_field = fields.Char()

class Students(Session):
	_name = 'openacademy.students'
	_description = "OpenAcademy Students"

	student_name = fields.Char(required=True)
	student_email = fields.Char()
	student_course = Session.name
	student_attandance = fields.Integer()
	

