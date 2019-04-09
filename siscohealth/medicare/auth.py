import logging
import requests
import frappe
from werkzeug.utils import redirect

logger = logging.getLogger('hhs_server.%s' % __name__)


class OAuth2Config():
    def __init__(self):
        self.authorized_url = "https://sandbox.bluebutton.cms.gov/v1/o/authorize/"
        self.token_url = "https://sandbox.bluebutton.cms.gov/v1/o/token/"
        self.setting = frappe.get_doc("Medicare Setting", "Medicare Setting")
        self.client_id = self.setting.client_id
        self.client_secret = self.setting.client_secret
        self.redirect_uri = self.setting.redirect_uri

    def get_headers(self):
            return {
                    "Authorization": "Basic %s:%s "%(self.client_id, self.client_secret)
                    }

    def send_request(self):
        url = self.get_url()
        logger.info(url)
        return redirect(url)

    def get_url(self):

        url = "%s?client_id=%s&redirect_uri=%s&response_type=code"%(
                        self.setting.url, self.client_id, self.redirect_uri)
        
        return url

    def get_access_token(self, code):
        url = "%s?code=%s&grant_type=authorization_code&redirect_uri=%s"%(
                    self.token_url, code, self.redirect_uri)
        print(url)
        self.sess = requests.Session()
        return self.sess.post(url, auth=self.get_basic_auth())

    def get_basic_auth(self):
            return (self.client_id, self.client_secret)

@frappe.whitelist(allow_guest=True)
def test_oauth(**kwargs):
        client = OAuth2Config()
        return client.send_request()

        print("navdeep")
