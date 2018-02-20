import falcon
from mail_delegater import MailDelegater
from falcon_cors import CORS

cors = CORS(allow_origins_list=['http://0.0.0.0:4000',
                                'https://www.nukapi.com:443'])
app = falcon.API(middleware=[cors.middleware])
app.req_options.auto_parse_form_urlencoded = True
mailDelegater = MailDelegater()
app.add_route('/forms', mailDelegater)