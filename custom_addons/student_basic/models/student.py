from odoo import models, fields

class StudentBasic(models.Model):
    _name = 'student.basic'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    expiration_date = fields.Date(string="Expiration Date")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender')
    active = fields.Boolean(default=True)
    description = fields.Text(string='Description')



