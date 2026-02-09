# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrCosigner(models.Model):
    _name = 'hr.cosigner'
    _description = 'Employee Cosigner'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    # Image fields - same structure as hr.employee
    image_1920 = fields.Image("Photo", max_width=1920, max_height=1920)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)

    name = fields.Char(string='Full Name', required=True, tracking=True)
    phone = fields.Char(string='Phone Number', tracking=True)
    
    # Relation to employee
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
        ondelete='cascade',
        index=True,
    )
    
    # Document attachments - using ir.attachment relation
    attachment_ids = fields.Many2many(
        'ir.attachment',
        'hr_cosigner_attachment_rel',
        'cosigner_id',
        'attachment_id',
        string='Document Attachments',
    )
    attachment_count = fields.Integer(
        string='Attachment Count',
        compute='_compute_attachment_count',
    )
    
    # Additional useful fields
    signing_date = fields.Date(
        string='Signing Date',
        tracking=True,
        help='Date when the cosigner signed for the employee',
    )
    company_id = fields.Many2one(
        related='employee_id.company_id',
        string='Company',
        store=True,
    )
    active = fields.Boolean(default=True)
    notes = fields.Text(string='Notes')

    # =============================================
    # Private Information Fields
    # =============================================

    # Living Address
    woreda = fields.Char(string="Woreda")
    house_number = fields.Char(string='House Number', tracking=True)
    city = fields.Char(string='City', tracking=True)
    state_id = fields.Many2one(
        'res.country.state',
        string='State',
        tracking=True,
        domain="[('country_id', '=', country_id)]",
    )
    country_id = fields.Many2one(
        'res.country',
        string='Country',
        tracking=True,
    )

    # Work Information
    work_type = fields.Selection([
        ('private', 'Private Company Employee'),
        ('governmental', 'Government Employee'),
    ], string='Type of Employment', tracking=True)
    work_field = fields.Char(string='Job Title', tracking=True)
    working_company_name = fields.Char(string='Working Company Name', tracking=True)
    company_found_city = fields.Char(string='Company City', tracking=True)
    company_found_state = fields.Char(string='Company State', tracking=True)
    phone_number = fields.Char(string="Phone Number")


    # Financial Information
    monthly_wage = fields.Monetary(
        string='Cosigner Monthly Wage',
        tracking=True,
        currency_field='currency_id',
    )
    amount_given = fields.Monetary(
        string='Guaranteed Amount',
        tracking=True,
        currency_field='currency_id',
        help="Amount for which the guarantor is legally responsible"
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        default=lambda self: self.env.company.currency_id,
    )
    purpose_of_guarantee = fields.Char(
        string="Purpose of Guarantee",
        help="Enter the purpose of the guarantee for this order"
    )

    @api.depends('attachment_ids')
    def _compute_attachment_count(self):
        for record in self:
            record.attachment_count = len(record.attachment_ids)

    def action_view_attachments(self):
        """Open attachment view for this cosigner"""
        self.ensure_one()
        return {
            'name': 'Attachments',
            'type': 'ir.actions.act_window',
            'res_model': 'ir.attachment',
            'view_mode': 'kanban,tree,form',
            'domain': [('id', 'in', self.attachment_ids.ids)],
            'context': {
                'default_res_model': self._name,
                'default_res_id': self.id,
            },
        }
