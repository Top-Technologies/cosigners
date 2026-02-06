# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    cosigner_ids = fields.One2many(
        'hr.cosigner',
        'employee_id',
        string='Cosigners',
    )
    cosigner_count = fields.Integer(
        string='Cosigner Count',
        compute='_compute_cosigner_count',
    )

    @api.depends('cosigner_ids')
    def _compute_cosigner_count(self):
        for employee in self:
            employee.cosigner_count = len(employee.cosigner_ids)

    def action_open_cosigners(self):
        """Open cosigners list for this employee"""
        self.ensure_one()
        return {
            'name': 'Cosigners',
            'type': 'ir.actions.act_window',
            'res_model': 'hr.cosigner',
            'view_mode': 'kanban,list,form',
            'domain': [('employee_id', '=', self.id)],
            'context': {'default_employee_id': self.id},
        }
