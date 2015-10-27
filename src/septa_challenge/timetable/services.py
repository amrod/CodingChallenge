import requests


SEPTA_NEXTTOARRIVE_URL = "http://www3.septa.org/hackathon/NextToArrive"

def get_next_to_arrive(start_station, end_station):
    """
    Retrieves NextToArrive info from SEPTA.

    :param start_station: Start station
    :param end_station:  End station
    :return: a list of trains arriving at end_station from start_station
    """
    start_station = replace_amp(start_station)
    end_station = replace_amp(end_station)

    params = {'req1': start_station, 'req2': end_station}

    r = requests.get(SEPTA_NEXTTOARRIVE_URL, params=params)

    if r.status_code == 200:
        return r.json()
    return []

def replace_amp(s):
    """
    Replaces occurrences of ' & ' with '-' in s and returns the new string.
    :param s: String to make replacement in.
    :return: String with characters replaced.
    """
    return s.replace(' & ', '-')