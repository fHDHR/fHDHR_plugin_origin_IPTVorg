

class OriginEPG():

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

    def update_epg(self, fhdhr_channels):
        programguide = {}
        return programguide

        for fhdhr_id in list(fhdhr_channels.list.keys()):
            chan_obj = fhdhr_channels.list[fhdhr_id]

            filtered_chan_dict = fhdhr_channels.origin.get_channel_dict(fhdhr_channels.origin.filtered_chan_list, "name", chan_obj.dict["origin_name"])

            if str(chan_obj.number) not in list(programguide.keys()):
                programguide[str(chan_obj.number)] = chan_obj.epgdict

            if filtered_chan_dict["tvg"]["url"]:
                print(filtered_chan_dict["tvg"]["url"])

        return programguide
