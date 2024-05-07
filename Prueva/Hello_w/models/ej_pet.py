#-*- coding: utf-8 -*-
from odoo import api, fields, models

class Ejpet(models.Model):
    _name = 'ej.pet'
    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age', required=True)
    color = fields.Char(string='color', required=True)
    is_new = fields.Boolean(string='is_new', default=True)
    type = fields.Selection(
        selection=[
        ('dog','Dog'),
        ('cat','Cat'),
        ('fish','Fish'),
        ('other','Other')], string='type', default="dog", required=True)
