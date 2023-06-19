# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class DesignerCommission(models.Model):
	_name = 'designer.commission'

	designer_id = fields.Many2one('product.template', string='Product')
	partner_des_id = fields.Many2one('res.partner', string='Designers')
	partner_commission = fields.Integer(string='Royalty%')