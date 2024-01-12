from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _name = "emp.info"
    _description = " Employee Information"

    name = fields.Char(string="Name")
    emp_id = fields.Integer(string="Emp ID")
    dob = fields.Date(string="Date of Birth")
    enroll_date = fields.Datetime(string="Enroll Date")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")

    # Using of the create Method
    @api.model
    def create(self, vals):
        vals['name'] = vals['name'].capitalize()
        return super(Employee, self).create(vals)

    # Using of the Write Method
    def write(self, vals):
        res = super(Employee, self).write(vals)
        if 'dob' in vals:
            raise ValidationError(_('Dob not allow to change !!'))
        return res
