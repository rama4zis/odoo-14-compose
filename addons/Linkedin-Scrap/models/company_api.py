from odoo import fields, models 
import json
import requests
import pandas as pd
import io
import base64

from odoo.exceptions import Warning

class CompanyApi(models.Model):
    _name = 'company.api'
    _description = 'Linkedin Company API'

    # name = fields.Char(string="Name", required=True)
    # companyWebsite = fields.Char(string="Website", required=True)
    # companyPhone = fields.Char(string="Phone", required=True)
    # companyIndustry = fields.Char(string="Company Industry", required=True)
    # companyMembers = fields.Char(string="Company Members", required=True)
    # companyHeadOffice = fields.Char(string="Company Head Office", required=True)
    # companyStanding = fields.Char(string="Company Standing", required=True)
    # companySpeciality = fields.Char(string="Company Speciality", required=True)
    # companyLocation = fields.Char(string="Company Location", required=True)
    # companyFollowers = fields.Char(string="Company Followers", required=True)
    
    keyword = fields.Char(string="Keyword", required=True)
    fileResult = fields.Many2one(comodel_name="ir.attachment", string="File Result")
    result = fields.Binary(string="Excel Result", related='fileResult.datas')
    resultName = fields.Char(string="Result Name", related='fileResult.name')
    
    apiServer = "192.168.1.59"
    
    
    def search_company(self):
        querystring = self.keyword
        url = f"http://{self.apiServer}:8000/get/{querystring}"
        
        response = requests.get(url)
        return response
        
    def generate_data(self):
        querystring = self.keyword
        url = f"http://{self.apiServer}:8000/get/{querystring}"
        
        requests.post(url)
        # data = response.json()
        return "ok"
    
    def export_data(self):
        data = self.search_company()
        # raise Warning(
        #     f"Exported Successfully : {json.loads(data.text)}"
        # )
        data_dict = json.loads(data.text)
        data_list = data_dict["data"]
        df = pd.DataFrame(data_list)
        
        file_buffer = io.BytesIO()
        
        write = pd.ExcelWriter(file_buffer, engine='xlsxwriter')
        df.to_excel(write, index=False)
        write.save()
        
        # set to attachment file 
        excel_file = base64.b64encode(file_buffer.getvalue())
        excelResult = self.env['ir.attachment'].create({
            'name': f'{self.keyword}.xlsx',
            'type': 'binary',
            'datas': excel_file.decode('utf-8') 
        })
        
        self.fileResult = excelResult.id