import logging
import smtplib
import json
from email.mime.text import MIMEText
import os

MAIL_TEMPLATE = "Received Form Submission:\n FORM_DATA"


class MailDelegater(object):

    def on_get(self, req, resp):
        self.delegate_to_mail(req, resp)

    def on_post(self, req, resp):
        self.delegate_to_mail(req, resp)

    def delegate_to_mail(self, req, resp):
        msg_text = MAIL_TEMPLATE.replace("FORM_DATA", json.dumps(req.params,
                                                                     indent=4,
                                                                     sort_keys=True))
        # msg = MIMEText(msg_text)
        # msg['Subject'] = 'Formsubmission from www.nukapi.com'
        # msg['From'] = "formapi@nukapi.com"
        # msg['To'] = "sefidrodi@googlemail.com"

        logging.warning(msg_text)

        # s = smtplib.SMTP( os.environ.get("RELAYHOST", "localhost"))
        # s.send_message(msg)
        # s.quit()
        # logging.warning(MAIL_TEMPLATE.replace("FORM_DATA", req.params))