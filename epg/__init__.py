

class Plugin_OBJ():

    def __init__(self, channels, plugin_utils):
        self.plugin_utils = plugin_utils

        self.channels = channels

        self.origin_name = plugin_utils.origin_name

    def update_epg(self):
        programguide = {}
        return programguide

        for fhdhr_channel_id in list(self.channels.list.keys()):
            chan_obj = self.channels.list[fhdhr_channel_id]

            filtered_chan_dict = self.origin_obj.get_channel_dict(self.origin_obj.filtered_chan_list, "name", chan_obj.dict["origin_name"])

            if str(chan_obj.number) not in list(programguide.keys()):
                programguide[str(chan_obj.number)] = chan_obj.epgdict

            if filtered_chan_dict["tvg"]["url"]:
                print(filtered_chan_dict["tvg"]["url"])

        return programguide
