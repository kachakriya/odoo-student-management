from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")

    course_id = fields.Many2one('student.course',string="Course")# One student belongs to one course
    subject_ids = fields.Many2many('student.subject',string="Subjects")# One student can choose multiple subjects


