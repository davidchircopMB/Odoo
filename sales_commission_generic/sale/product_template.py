# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	designer_ids = fields.One2many('designer.commission', 'designer_id', string='Designer Commission')

	@api.constrains('designer_ids')
	def _check_designer_ids(self):
		if self.designer_ids:
			commission_obj = self.env['sale.commission'].search([('comm_type','=','mix')])
			exception_list =[]
			commission_precentage = 0
			for comm in commission_obj :
				exception_data = comm.exception_ids.mapped('based_on_2')
				exception_list.append(exception_data)

				for exc in comm.exception_ids : 
					if self.id == exc.product_id.product_tmpl_id.id:
						for des in self.designer_ids :
							commission_precentage += des.partner_commission

						if commission_precentage > exc.commission_precentage :
							raise ValidationError(_('Designer Royalties Exceptions Percentage is lower then Designers Commissions .'))

			combined_list = [item for sublist in exception_list for item in sublist]
			if self.designer_ids:
				if 'Royalty Exception' not in combined_list:
					raise ValidationError(_('Please add Designer Royalties Exceptions.'))