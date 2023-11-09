from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcyleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number'
    _sql_constraints = [
        ('vin_unique', 'UNIQUE(vin)','Odoopise! Another registration for this VIN number already exists.')
    ]
    
    certificate_title = fields.Binary(string='Certificate of Title')
    current_mileage = fields.Float(string='Current Mileage')
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    license_plate = fields.Char(string='License Plate Number')
    registry_date = fields.Date('Registration Date')
    registry_number = fields.Char('Registry Number', copy=False, required=True, readonly=True, default='New')
    vin = fields.Char(string='VIN', required=True)
    picture = fields.Image (string='Photograph')