import xml.etree.ElementTree as ET
from urllib.parse import urlencode

import requests

from .exceptions import HamQTHClientError, HamQTHClientNotFoundError

HAMQTH_URL = "https://www.hamqth.com/xml.php"

HAMQTH_NAMESPACE = {
    "hamqth": "https://www.hamqth.com",
}


class HamQTHClient:
    """
    https://www.hamqth.com/developers.php#xml_search
    """
    def __init__(self, session_id=None, program_name=None):
        self.session_id = session_id if session_id is not None else None
        self.program_name = program_name if program_name is not None else self.__class__.__name__

    def authenticate(self, username, password):
        session_id = self.get_session_id(username, password)
        self.session_id = session_id

    @property
    def is_authenticated(self):
        return self.session_id is not None

    def logout(self):
        self.session_id = None

    def search_callsign(self, query):
        if not self.is_authenticated:
            raise HamQTHClientError('client must authenticate to perform callsign search')
        search_query = payload = dict(id=self.session_id, callsign=query, prg=self.program_name)
        response = self.request(HAMQTH_URL, payload=search_query)
        root = ET.fromstring(response.text)
        search = root.find("hamqth:search", HAMQTH_NAMESPACE)
        if search is None:
            session = root.find("hamqth:session", HAMQTH_NAMESPACE)
            error = session.find("hamqth:error", HAMQTH_NAMESPACE)
            raise HamQTHClientNotFoundError(error.text)
        return search

    def search_callsign_bio(self, query, strip_html=True):
        if not self.is_authenticated:
            raise HamQTHClientError('client must authenticate to perform callsign search')
        search_query = payload = dict(id=self.session_id, callsign=query, strip_html=int(strip_html))
        response = self.request(HAMQTH_URL, payload=search_query)
        root = ET.fromstring(response.text)
        search = root.find("hamqth:search", HAMQTH_NAMESPACE)
        if search is None:
            session = root.find("hamqth:session", HAMQTH_NAMESPACE)
            error = session.find("hamqth:error", HAMQTH_NAMESPACE)
            raise HamQTHClientNotFoundError(error.text)
        return search

    def search_callsign_recent_activity(self, query, rec_activity=True, log_activity=True, logbook=True):
        if not self.is_authenticated:
            raise HamQTHClientError('client must authenticate to perform callsign search')
        search_query = payload = dict(id=self.session_id, callsign=query, rec_activity=int(rec_activity), log_activity=int(log_activity), logbook=int(logbook))
        response = self.request(HAMQTH_URL, payload=search_query)
        root = ET.fromstring(response.text)
        search = root.find("hamqth:search", HAMQTH_NAMESPACE)
        if search is None:
            session = root.find("hamqth:session", HAMQTH_NAMESPACE)
            error = session.find("hamqth:error", HAMQTH_NAMESPACE)
            raise HamQTHClientNotFoundError(error.text)
        return search

    def get_session_id(self, username, password):
        credentials = dict(u=username, p=password)
        response = self.request(HAMQTH_URL, payload=credentials)
        root = ET.fromstring(response.text)
        session = root.find("hamqth:session", HAMQTH_NAMESPACE)
        session_id = session.find("hamqth:session_id", HAMQTH_NAMESPACE)
        if session_id is None:
            error = session.find("hamqth:error", HAMQTH_NAMESPACE)
            raise HamQTHClientError('Could not get session ID', error.text)
        return session_id.text

    def request(self, url, payload=None):
        response = requests.get(url, params=urlencode(payload))
        if not response.ok:
            response.raise_for_status()
        return response
