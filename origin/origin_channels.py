

class OriginChannels():

    def __init__(self, fhdhr, origin):
        self.fhdhr = fhdhr
        self.origin = origin

        self.unfiltered_chan_json = None
        self.filtered_chan_json = None

    @property
    def filtered_chan_list(self):
        if not self.filtered_chan_json:
            self.filtered_chan_json = self.filterlist()
        return self.filtered_chan_json

    @property
    def unfiltered_chan_list(self):
        if not self.unfiltered_chan_json:
            self.unfiltered_chan_json = self.get_unfiltered_chan_json()
        return self.unfiltered_chan_json

    def get_channels(self):

        channel_list = []

        self.fhdhr.logger.info("Pulling Unfiltered Channels: %s" % self.origin.channels_json_url)
        self.unfiltered_chan_json = self.get_unfiltered_chan_json()
        self.fhdhr.logger.info("Found %s Total Channels" % len(self.unfiltered_chan_json))

        self.filtered_chan_json = self.filterlist()
        self.fhdhr.logger.info("Found %s Channels after applying filters and Deduping." % len(self.filtered_chan_list))

        for channel_dict in self.filtered_chan_list:
            clean_station_item = {
                                 "name": channel_dict["name"],
                                 "id": channel_dict["name"],
                                 "thumbnail": channel_dict["logo"],
                                 }
            channel_list.append(clean_station_item)

        return channel_list

    def get_channel_stream(self, chandict, stream_args):
        streamdict = self.get_channel_dict(self.filtered_chan_list, "name", chandict["origin_name"])
        streamurl = streamdict["url"]

        stream_info = {"url": streamurl}

        return stream_info

    def get_unfiltered_chan_json(self):
        urlopn = self.fhdhr.web.session.get(self.origin.channels_json_url)
        return urlopn.json()

    def filterlist(self):

        filtered_chan_list = []
        for channels_item in self.unfiltered_chan_list:
            filters_passed = []
            for filter_key in list(self.origin.filter_dict.keys()):

                if not len(self.origin.filter_dict[filter_key]):
                    filters_passed.append(True)
                else:
                    if filter_key in ["country", "language"]:
                        if isinstance(channels_item[filter_key], list):
                            if len(channels_item[filter_key]):
                                chan_values = []
                                chan_values.extend([x["name"] for x in channels_item[filter_key]])
                                chan_values.extend([x["code"] for x in channels_item[filter_key]])
                            else:
                                chan_values = []
                        else:
                            chan_values = []
                            chan_values.append(channels_item[filter_key]["name"])
                            chan_values.append(channels_item[filter_key]["code"])
                    elif filter_key in ["category"]:
                        chan_values = [channels_item[filter_key]]

                    if not len(chan_values):
                        filter_passed = False
                    else:
                        values_passed = []
                        for chan_value in chan_values:
                            if str(chan_value).lower() in [x.lower() for x in self.origin.filter_dict[filter_key]]:
                                values_passed.append(True)
                            else:
                                values_passed.append(False)
                        if True in values_passed:
                            filter_passed = True
                        else:
                            filter_passed = False

                    filters_passed.append(filter_passed)

            if False not in filters_passed:
                if channels_item["name"] not in [x["name"] for x in filtered_chan_list]:
                    filtered_chan_list.append(channels_item)

        return filtered_chan_list

    def get_channel_dict(self, chanlist, keyfind, valfind):
        return next(item for item in chanlist if item[keyfind] == valfind) or None
