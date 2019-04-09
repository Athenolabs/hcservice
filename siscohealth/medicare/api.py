
import frappe
from six import string_types
from siscohealth.medicare.auth import OAuth2Config
@frappe.whitelist()
def  redirect(**kwargs):
        doc = frappe.get_doc("Medicare Setting", "Medicare Setting")
        if kwargs and isinstance(kwargs, string_types):
                kwargs = json.loads(kwargs)

        code = kwargs.get("code")
        client = OAuth2Config()
        res = client.get_access_token(code)
        print(res.json())
        
