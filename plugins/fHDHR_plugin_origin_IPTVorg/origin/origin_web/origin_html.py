from flask import request, render_template_string
import pathlib
from io import StringIO


class Origin_HTML():
    endpoints = ["/origin", "/origin.html"]
    endpoint_name = "page_origin_html"

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

        self.template_file = pathlib.Path(self.fhdhr.config.internal["paths"]["origin_web"]).joinpath('origin.html')
        self.template = StringIO()
        self.template.write(open(self.template_file).read())

    def __call__(self, *args):
        return self.get(*args)

    def get(self, *args):

        if self.fhdhr.originwrapper.setup_success:
            origin_status_dict = {"Setup": "Success"}
            origin_status_dict["Total Channels"] = len(self.fhdhr.device.channels.list)
        else:
            origin_status_dict = {"Setup": "Failed"}
        return render_template_string(self.template.getvalue(), request=request, fhdhr=self.fhdhr, origin_status_dict=origin_status_dict, list=list)
