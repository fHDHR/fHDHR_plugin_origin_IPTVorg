

class OriginService():

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

        self.channels_json_url = "https://iptv-org.github.io/iptv/channels.json"

        self.filter_dict = {}
        self.setup_filters()

    def setup_filters(self):

        for x in ["country", "language", "category"]:
            self.filter_dict[x] = []

        for filter in list(self.filter_dict.keys()):

            filterconf = self.fhdhr.config.dict["origin"]["filter_%s" % filter]
            if filterconf:
                if isinstance(filterconf, str):
                    filterconf = [filterconf]
                self.fhdhr.logger.info("Found %s Enabled %s Filters" % (len(filterconf), filter))
                self.filter_dict[filter].extend(filterconf)
            else:
                self.fhdhr.logger.info("Found No Enabled %s Filters" % (filter))
