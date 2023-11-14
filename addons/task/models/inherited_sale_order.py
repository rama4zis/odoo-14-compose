from odoo import fields, models, api, _
from odoo.exceptions import Warning

class InheritedSaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"
    _description = "This Sales Order Inherit"

    is_booking_order = fields.Boolean()
    team_name = fields.Many2one(comodel_name = "service_team", required=True)
    team_leader = fields.Many2one(comodel_name = "res.users", related='team_name.team_leader')
    # team_members = fields.Many2many(comodel_name = "res.users")
    # team members only get the name fields from res.users 
    team_members = fields.Many2many(comodel_name = "res.users", related='team_name.team_members')
    booking_start = fields.Datetime(comodel_name = "Booking Start", required=True)
    booking_end = fields.Datetime(comodel_name = "Booking End", required=True)

    # Check if each of team and team leader already active Work Order( Which not cancelled ) where planned start and planned end is overlap with booking start and booking end from sale.order :
    def check_work_order(self):
        work_orders = self.env['work_order'].search([
            ('state', '!=', 'cancelled'),
            ('planned_start', '<=', self.booking_end),
            ('planned_end', '>=', self.booking_start),
            ('team_name', '=', self.team_name.id),
            ('team_leader', '=', self.team_leader.id)
        ])
        print("---------------------------------")
        print(work_orders)
        print("---------------------------------")
        # work_order_book_ref = 

        # if there is overlap, then popup "Team already has work order during that period on $sale.order.name"
        if work_orders:
            # print(work_orders)
            # raise RedirectWarning(
            #     _("Team already has work order during that period on %s" % work_orders[0].booking_order_ref.name)
            #     # _(work_orders)
            # )
            
            raise Warning (
                "Team already has work order during that period on %s" % work_orders[0].booking_order_ref.name
            )
        else:
            # if there is no overlap, ten popup "Team is available for booking"
            # raise RedirectWarning(
            #     _("Team is available for booking")
            # )
            
            raise Warning (
                "Team is available for booking"
            )

    # Make onchange team name, auto fill team member and team leader 
    @api.onchange('team_name')
    def _onchange_(self):
        if self.team_name:
            self.team_leader = self.team_name.team_leader
            self.team_members = self.team_name.team_members
        else:
            self.team_leader = False
            self.team_members = False

        pass
