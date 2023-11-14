{
	"name": "Academic Information System Day 3",
	"version": "1.0", 
	"depends": [
		"base",
		"account",
		"sale",
	],
	"author": "akhmad.daniel@gmail.com", 
	"category": "Education", 
	'website': 'http://www.vitraining.com',
	"description": """\
Academic Information System Day 3

""",
	"data": [
		# Menu
        "menu.xml",
        
        # Views
        "views/attendee_view.xml",
        "views/course_view.xml",
        "views/partner_view.xml",
        "views/session_view.xml",
        
        # Report
        "report/session_report_view.xml",
        
        # Security
        "security/ir.model.access.csv",
        "security/groups.xml",
        
		
    
	],
}