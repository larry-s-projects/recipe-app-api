# from unittest.mock import patch
# from django.core.management import call_command
# from django.db.utils import OperationalError
# from django.test import TestCase
#
#
# class CommandTests(TestCase):
#
#     def test_wait_for_db_ready(self):
#         """Test waiting for db when db is availabe"""
#         with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
#             gi.return_value = True
#             call_command('wait_for_db')
#             self.assertEqual(gi.call_count, 1)
#
#     @patch('time.sleep', return_value=True) # We have this here because we dont actually need 5 seconds to retry the connection
#     def test_wait_for_db(self, ts ):
#         """Test waiting for db"""
#
#         with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
#             gi.side_effect = [OperationalError] * 5 + [True] # Raise error 5 times and on the 6 times it will return true
#             call_command('wait_for_db')
#             self.assertEqual(gi.call_count, 6) # calling the function 6 times
#
