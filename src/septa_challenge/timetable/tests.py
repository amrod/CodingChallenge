from django.test import TestCase
import mock
import services

class SEPTAServicesTestCases(TestCase):

    def setUp(self):
        self.a = 'Swarthmore'
        self.b = '30th Street Station'

    @mock.patch('timetable.services.requests')
    def test_get_next_to_arrive(self, mock_requests):
        """Verify get_next_to_arrive performs a get request with proper
        parameters.
        """

        r = services.get_next_to_arrive(self.a, self.b)
        params = {'req1': self.a, 'req2': self.b}

        self.assertTrue(
            mock.call.get(services.SEPTA_NEXTTOARRIVE_URL, params=params) in
            mock_requests.mock_calls)

    @mock.patch('timetable.services.requests')
    def test_get_next_to_arrive_ampersand(self, mock_requests):
        """Verify ampersand is handled correctly.
        """

        r = services.get_next_to_arrive(self.a, 'Airport Terminals E & F')
        params = {'req1': self.a, 'req2': 'Airport Terminals E-F'}

        self.assertTrue(
            mock.call.get(services.SEPTA_NEXTTOARRIVE_URL, params=params) in
            mock_requests.mock_calls)
