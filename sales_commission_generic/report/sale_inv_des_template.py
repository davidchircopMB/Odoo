# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _
import operator


class sale_inv_des_template(models.AbstractModel):
	_name = 'report.sales_commission_generic.sale_inv_des_template'
	_description = 'Report sale inv des template'

	def _get_report_values(self, docids, data=None):
		
		record_ids = self.env[data['model']].browse(data['form'])

		currency_ids = []
		sum_dict = {}
		
		for i in record_ids:
			if i.currency_id:
				currency_ids.append({'currency_id': i.currency_id.id, 'commission_amount':i.commission_amount})

		sorted_data = sorted(currency_ids, key=operator.itemgetter('currency_id'))

		for item in sorted_data:
			currency_id = item['currency_id']
			commission_amount = item['commission_amount']
			sum_dict[currency_id] = sum_dict.get(currency_id, 0) + commission_amount

		final_list = [{'currency_id': currency_id, 'commission_amount': sum_dict[currency_id]} for currency_id in sum_dict]

		return {
					'doc_ids': self.ids,
					'doc_model': data['model'],
					'docs': self,
					'data' : data,
					'ids':record_ids,
					'total_result': final_list
				}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
