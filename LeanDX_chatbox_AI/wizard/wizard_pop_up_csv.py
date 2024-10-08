from odoo import models, fields, api


class Upload_csv_pop_up(models.TransientModel):
    _name = 'LeanDX.chatBox_AI.upload.csv'
    _description = 'Upload CSV Pop Up'

    """
        This Model is used to upload a CSV file.
        CSV have column name.
            We have to ensure that the columns are right.
        
    """
        #TODO: Manage CSV columns semantic.
    name = fields.Char(string='Name')
    file = fields.File(string='File')


    columns = fields.One2many('LeanDX.chatBox_AI.upload.csv.column', 'csv_file', string='Columns')

    def add_column(self):
        self.env['LeanDX.chatBox_AI.upload.csv.column'].create({
            'csv_file': self.id
        })
        #reload the form view.




    def upload_csv(self):
        pass


class column_csv_pop_up(models.TransientModel):
    _name = 'LeanDX.chatBox_AI.upload.csv.column'
    _description = 'Column CSV Pop Up'

    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    csv_file = fields.Many2one('upload.csv.pop.up', string='CSV File')

