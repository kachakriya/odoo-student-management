from odoo import models, fields

class Subject(models.Model):
    _name = 'student.subject'
    _description = 'Subject'

    name = fields.Char(string="Subject Name", required=True)# One subject can have multiple Student
    student_ids = fields.Many2many('student.student',string="Students")# One Student can enroll in multiple subject