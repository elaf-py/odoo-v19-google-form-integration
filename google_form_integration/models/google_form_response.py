from odoo import models, fields


class GoogleWorkerResponse(models.Model):
    _name = 'google.worker.response'
    _description = 'Google Worker Response'
    _order = 'submission_date desc'

    submission_date = fields.Datetime(
        string='Submission Date'
    )

    email = fields.Char(
        string='Email Address'
    )

    worker_name = fields.Char(
        string='Full Worker Name',
        required=True
    )

    project_name = fields.Char(
        string='Project'
    )

    work_date = fields.Date(
        string='Date Of Work'
    )

    photo_links = fields.Text(
        string='Photos'
    )