from flask import request, render_template_string, session
import pathlib
from io import StringIO


class Origin_HTML():
    endpoints = ["/iptvorg", "/iptvorg.html"]
    endpoint_name = "page_iptvorg_html"
    endpoint_category = "pages"
    pretty_name = "IPTVorg"

    def __init__(self, fhdhr, plugin_utils):
        self.fhdhr = fhdhr
        self.plugin_utils = plugin_utils

        self.origin = plugin_utils.origin

        self.template_file = pathlib.Path(plugin_utils.path).joinpath('origin.html')
        self.template = StringIO()
        self.template.write(open(self.template_file).read())

    def __call__(self, *args):
        return self.get(*args)

    def get(self, *args):

        if self.origin.setup_success:
            origin_status_dict = {"Setup": "Success"}
        else:
            origin_status_dict = {"Setup": "Failed"}
        return render_template_string(self.template.getvalue(), request=request, session=session, fhdhr=self.fhdhr, origin_status_dict=origin_status_dict, list=list, origin=self.plugin_utils.namespace)
