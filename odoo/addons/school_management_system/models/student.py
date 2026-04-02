from odoo import fields, models


class Student(models.Model):
    _name = 'school.school'
    _description = 'Student'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone", required=True)
    address = fields.Char(string="Address")
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender"
    )
    expiration_date = fields.Date(string="Expiration Date")
    partner_id = fields.Many2one('res.partner')
    class_data = fields.Many2one('class.data', string="Class Data")

class ClassData(models.Model):
        _name = 'class.data'

        name = fields.Char('Class Name')



