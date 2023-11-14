from odoo import fields, models

class ServiceTeam(models.Model):
    _name = "service_team"
    _description = "Service Team"
    _rec_name = "team_name"

    # List Field 
    team_name = fields.Char(string="Team Name", required=True)
    team_leader = fields.Many2one(comodel_name = "res.users", string="Team Leader")
    team_members = fields.Many2many(comodel_name = "res.users", string="Team Members")

    sequence = fields.Integer(string='Sequence', default=0)