from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'   
    
    name = fields.Char(string="Motorcycle Registry")
    
    registry_number = fields.Char(string='Registry Number', default="MRN0000", copy=False, required=True, readonly=True)
    certificate_title = fields.Binary(string='Certificate of Title')
    current_mileage = fields.Float(string='Current Mileage')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    license_plate = fields.Char(string='License Plate Number')
    registry_date = fields.Date('Registration Date')
    vin = fields.Char(string='VIN', required=True)
    picture = fields.Image (string='Photograph')
    active = fields.Boolean(default=True)
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)