from odoo import models, fields

class Course(models.Model):
    _name = 'student.course'
    _description = 'Course'

    name = fields.Char(string="Course Name", required=True)
    # One course can have multiple students
    student_ids = fields.One2many('student.student','course_id',string="Students")