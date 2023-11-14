from odoo import api, fields, models

class WorkOrder(models.Model):
    _name = "work_order"
    _description = "This Work Order Object Model"
    
    # For generate WO Number 
    name = fields.Char( string="Work Order Number" )
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('sequence_work_order_code')
        return super(WorkOrder, self).create(vals)

    booking_order_ref = fields.Many2one(comodel_name = "sale.order", readonly = False)
    team_name = fields.Many2one(comodel_name = "service_team", required = True)
    team_leader = fields.Many2one(comodel_name = "res.users", related='team_name.team_leader')
    team_members = fields.Many2many(comodel_name = "res.users", related='team_name.team_members')
    planned_start = fields.Datetime(required = True)
    planned_end = fields.Datetime(required = True)
    date_start = fields.Datetime(required = True)
    date_end = fields.Datetime(required = True)
    state = fields.Selection(string="Status", required=True, readonly=True, default="pending", tracking=True,
        selection = [
            ("pending", "Pending"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ]
    )
    notes = fields.Text()
    
    rel_customer = fields.Many2one(comodel_name = "res.partner", related='booking_order_ref.partner_id')

    @api.onchange('team_name')
    def _onchange_(self):
        if self.team_name:
            self.team_leader = self.team_name.team_leader
            self.team_members = self.team_name.team_members
        else:
            self.team_leader = False
            self.team_members = False

    
    def action_pending(self):
        self.write({ 'state': "pending" })

    
    def action_in_progress(self):
        self.write({ 'state': "in_progress" })

    
    def action_done(self):
        self.write({ 'state': "done" })

    
    def action_cancelled(self):
        self.write({ 'state': "cancelled" })