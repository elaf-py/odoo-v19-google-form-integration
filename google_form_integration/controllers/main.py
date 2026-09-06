from odoo import http
from odoo.http import request


class GoogleWorkerController(http.Controller):

    @http.route(
        '/api/google-worker-response',
        type='json',
        auth='public',
        methods=['POST'],
        csrf=False
    )
    def google_worker_response(self, **kwargs):

        data = request.jsonrequest

        record = request.env[
            'google.worker.response'
        ].sudo().create({
            'email': data.get('email'),
            'worker_name': data.get('worker_name'),
            'project_name': data.get('project'),
            'work_date': data.get('work_date'),
            'photo_links': data.get('photos'),
        })

        return {
            'success': True,
            'record_id': record.id,
        }