from odoo import api, fields, models
from odoo.exceptions import ValidationError

class MotorcyleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry'
    _rec_name = 'registry_number'
    _sql_constraints = [
        ('vin_unique', 'UNIQUE(vin)','Odoopise! Another registration for this VIN number already exists.')
    ]
    
    registry_number = fields.Char('Registry Number', copy=False, required=True, readonly=True, default='New')
    vin = fields.Char(string='VIN', required=True)
    first_name = fiels.Char(string='First Name', required=True)
    last_name = fiels.Char(string='Last Name', required=True)
    picture = fields.Image (string='Photograph')
    current_mileage = fields.Float(string='Current Mileage')
    license_plate = fields.Char(string='License Plate Number')
    certificate_title = fields.Binary(string='Certificate of Title')
    registry_date = fields.Date('Registration Date')
    
    #Owner Fields
    owner_id = fields.Many2One(comodel_name = 'res.partner', ondelete='restrict')