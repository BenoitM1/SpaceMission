from odoo import models, fields


class Spaceship (models.Model):
    _name = 'spaceship.spaceship'

    name = fields.Char(string="Name")
    crew_capacity = fields.Integer(string="Equipage maximum")
    fuel_type = fields.Selection(selection=[('solide', 'Solide'), ('liquide', 'Liquide')], string="Type de carburant")
