from unittest import TestCase
from unittest.mock import patch

import requests

from hamqth.clients import HamQTHClient, HamQTHClientError, HamQTHClientNotFoundError

from .mock_responses import (
    SearchCallsignBioNotFoundResponse,
    SearchCallsignBioResponse,
    SearchCallsignNotFoundResponse,
    SearchCallsignRecentActivityNotFoundResponse,
    SearchCallsignRecentActivityResponse,
    SearchCallsignResponse,
    SessionIDRequestFailedResponse,
    SessionIDRequestResponse,
)


class HamQTHClientInitializationDefaultsTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient()

    def test_default_session_id_value(self):
        self.assertEqual(self.client.session_id, None)

    def test_default_program_name_value(self):
        self.assertEqual(self.client.program_name, 'HamQTHClient')


class HamQTHClientInitializeWithSessionIdTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient(session_id='test-session-id')

    def test_initialize_session_id_is_set(self):
        self.assertEqual(self.client.session_id, 'test-session-id')


class HamQTHClientInitializeWithProgramNameTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient(program_name='test-program-name')

    def test_initialize_program_name_is_set(self):
        self.assertEqual(self.client.program_name, 'test-program-name')


class HamQTHClientAuthenticateTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient()

    def test_authenticate(self):
        credentials = {'username': 'username', 'password': 'password'}
        with patch.object(HamQTHClient, 'request', return_value=SessionIDRequestResponse()) as mock_method:
            self.client.authenticate(**credentials)
        self.assertEqual(self.client.session_id, '09b0ae90050be03c452ad235a1f2915ad684393c')
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'u': 'username', 'p': 'password'})

    def test_authenticate_with_invalid_credentials(self):
        credentials = {'username': 'bad-username', 'password': 'or-bad-password'}
        with patch.object(HamQTHClient, 'request', return_value=SessionIDRequestFailedResponse()) as mock_method:
            with self.assertRaises(HamQTHClientError):
                self.client.authenticate(**credentials)
            self.assertTrue(self.client.session_id is None)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'u': 'bad-username', 'p': 'or-bad-password'})


class HamQTHClientRequestTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        class OkResponse:
            ok = True
        cls._response = OkResponse

    def setUp(self):
        self.client = HamQTHClient()

    def test_request(self):
        url = 'https://some-url.test/'
        payload = {'foo': 'bar'}
        with patch.object(requests, 'get', return_value=self._response()) as mock_method:
            self.client.request(url, payload=payload)
        mock_method.assert_called_once_with('https://some-url.test/', params='foo=bar')


class HamQTHClientRequestNotOkTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        class RaisedError(Exception): pass
        class NotOkResponse:
            ok = False
            def raise_for_status(self):
                raise RaisedError("raise_for_status was called")
        
        cls._raised_error = RaisedError
        cls._response = NotOkResponse

    def setUp(self):
        self.client = HamQTHClient()

    def test_request_not_ok_raises(self):
        url = 'https://some-url.test/'
        payload = {'foo': 'bar'}
        with patch.object(requests, 'get', return_value=self._response()) as mock_method:
            with self.assertRaises(self._raised_error):
                self.client.request(url, payload=payload)
        mock_method.assert_called_once_with('https://some-url.test/', params='foo=bar')


class HamQTHClientAuthenticatedTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient(session_id='abc123')

    def test_is_authenticated_is_true(self):
        self.assertTrue(self.client.is_authenticated)


class HamQTHClientNotAuthenticatedTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient()

    def test_is_authenticated_is_false(self):
        self.assertFalse(self.client.is_authenticated)

    def test_search_callsign_raises_error(self):
        with self.assertRaises(HamQTHClientError):
            self.client.search_callsign('abc123')

    def test_search_callsign_bio_raises_error(self):
        with self.assertRaises(HamQTHClientError):
            self.client.search_callsign_bio('abc123')

    def test_search_callsign_recent_activity_raises_error(self):
        with self.assertRaises(HamQTHClientError):
            self.client.search_callsign_recent_activity('abc123')


class HamQTHClientLogoutTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient(session_id='abc123')

    def test_logout(self):
        self.client.logout()
        self.assertTrue(self.client.session_id is None)


class HamQTHClientSearchCallsignTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient(session_id='09b0ae90050be03c452ad235a1f2915ad684393c')

    def test_search_callsign(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignResponse()) as mock_method:
            self.client.search_callsign(query)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'prg': 'HamQTHClient'})

    def test_search_callsign_not_found(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignNotFoundResponse()) as mock_method:
            with self.assertRaises(HamQTHClientNotFoundError):
                self.client.search_callsign(query)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'prg': 'HamQTHClient'})


class HamQTHClientSearchCallsignBioTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient(session_id='09b0ae90050be03c452ad235a1f2915ad684393c')

    def test_search_callsign_bio(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignBioResponse()) as mock_method:
            self.client.search_callsign_bio(query)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'strip_html': 1})

    def test_search_callsign_bio_strip_html(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignBioResponse()) as mock_method:
            self.client.search_callsign_bio(query, strip_html=False)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'strip_html': 0})

    def test_search_callsign_bio_not_found(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignBioNotFoundResponse()) as mock_method:
            with self.assertRaises(HamQTHClientNotFoundError):
                self.client.search_callsign_bio(query)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'strip_html': 1})


class HamQTHClientSearchCallsignRecentActivityTestCase(TestCase):
    def setUp(self):
        self.client = HamQTHClient(session_id='09b0ae90050be03c452ad235a1f2915ad684393c')

    def test_search_callsign_bio(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignRecentActivityResponse()) as mock_method:
            self.client.search_callsign_recent_activity(query)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'rec_activity': 1, 'log_activity': 1, 'logbook': 1})

    def test_search_callsign_bio_rec_activity(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignRecentActivityResponse()) as mock_method:
            self.client.search_callsign_recent_activity(query, rec_activity=False)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'rec_activity': 0, 'log_activity': 1, 'logbook': 1})

    def test_search_callsign_bio_log_activity(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignRecentActivityResponse()) as mock_method:
            self.client.search_callsign_recent_activity(query, log_activity=False)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'rec_activity': 1, 'log_activity': 0, 'logbook': 1})

    def test_search_callsign_bio_logbook(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignRecentActivityResponse()) as mock_method:
            self.client.search_callsign_recent_activity(query, logbook=False)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'rec_activity': 1, 'log_activity': 1, 'logbook': 0})

    def test_search_callsign_bio_not_found(self):
        query = 'ok2cqr'
        with patch.object(HamQTHClient, 'request', return_value=SearchCallsignRecentActivityNotFoundResponse()) as mock_method:
            with self.assertRaises(HamQTHClientNotFoundError):
                self.client.search_callsign_recent_activity(query)
        mock_method.assert_called_once_with('https://www.hamqth.com/xml.php', payload={'id': '09b0ae90050be03c452ad235a1f2915ad684393c', 'callsign': 'ok2cqr', 'rec_activity': 1, 'log_activity': 1, 'logbook': 1})
