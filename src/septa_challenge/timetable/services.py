import requests


SEPTA_NEXTTOARRIVE_URL = "http://www3.septa.org/hackathon/NextToArrive"

class SEPTAServices(object):

    def get_next_to_arrive(self, start_station, end_station):
        start_station = self.replace_amp(start_station)
        end_station = self.replace_amp(end_station)

        params = {'req1': start_station, 'req2': end_station}
        r = requests.get(SEPTA_NEXTTOARRIVE_URL, params=params)
        return r.json()

    def replace_amp(self, s):
        return s.replace(' & ', '-')