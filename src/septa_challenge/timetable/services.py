import requests


SEPTA_NEXTTOARRIVE_URL = "http://www3.septa.org/hackathon/NextToArrive"

def get_next_to_arrive(start_station, end_station):
    start_station = replace_amp(start_station)
    end_station = replace_amp(end_station)

    params = {'req1': start_station, 'req2': end_station}

    r = requests.get(SEPTA_NEXTTOARRIVE_URL, params=params)

    if r.status_code == 200:
        return r.json()
    return []

def replace_amp(s):
    return s.replace(' & ', '-')