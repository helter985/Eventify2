# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.event import Event  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEventController(BaseTestCase):
    """EventController integration test stubs"""

    def test_events_id_inscriptions_guid_get(self):
        """Test case for events_id_inscriptions_guid_get

        Find event by ID
        """
        response = self.client.open(
            '/api/v3/events/{id}/inscriptions/{guid}'.format(event_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_events_by_status(self):
        """Test case for find_events_by_status

        Finds Events by status
        """
        query_string = [('status', 'available')]
        response = self.client.open(
            '/api/v3/events/',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_event_by_id(self):
        """Test case for get_event_by_id

        Find event by ID
        """
        response = self.client.open(
            '/api/v3/events/{id}'.format(event_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_event_with_form(self):
        """Test case for update_event_with_form

        Inscription in an event
        """
        query_string = [('name', 'name_example'),
                        ('surname', 'surname_example'),
                        ('telephone', 56),
                        ('dni', 56),
                        ('mail', 'mail_example')]
        response = self.client.open(
            '/api/v3/events/{id}/inscriptions'.format(event_id=789),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upload_file(self):
        """Test case for upload_file

        
        """
        body = Object()
        response = self.client.open(
            '/api/v3/events/{id}/inscriptions/{invitation-code}'.format(invitation_code=789),
            method='DELETE',
            data=json.dumps(body),
            content_type='application/octet-stream')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
