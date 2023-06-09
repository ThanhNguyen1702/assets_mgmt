import base64
import logging
from odoo import http
from odoo.http import request


class ImageUrl(http.Controller):

    @http.route('/lf/i/<string:encodedimage>', type='http', auth='public')
    def create_image_url(self, encodedimage='', **kwargs):
        """
        This method is used to get image based on URL for in common product image model.URL will be generated
        automatically in ERP.
        :param encodedimage: Binary data
        :param kwargs: kwargs
        :return: Binary data of image
        """
        if encodedimage:
            try:
                decode_data = base64.urlsafe_b64decode(encodedimage)
                res_id = str(decode_data, "utf-8")
                status, headers, content = request.env['ir.http'].sudo().binary_content(
                        model='ir.attachment', id=res_id,
                        field='datas')
                content_base64 = base64.b64decode(content) if content else ''
                headers.append(('Content-Length', len(content_base64)))
                return request.make_response(content_base64, headers)
            except Exception:
                return request.not_found()
        return request.not_found()
