
from .origin_html import Origin_HTML


class Plugin_OBJ():

    def __init__(self, fhdhr, plugin_utils):
        self.fhdhr = fhdhr
        self.plugin_utils = plugin_utils

        self.origin_html = Origin_HTML(fhdhr, plugin_utils)
