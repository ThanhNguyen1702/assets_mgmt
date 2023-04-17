import odoo.http as http
from odoo.http import request
from odoo.tools import plaintext2html


class CheckApi(http.Controller):
    @http.route('/api/check',  methods=['GET'] , type='http', auth='none')
    def PrintSth(self, **kw):
        return "Hello World"