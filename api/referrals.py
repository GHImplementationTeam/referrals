from django.views.generic.base import View
from utils import json_response


class ReferralsView(View):
    @staticmethod
    def get(request):
        '''Retrieve all referrals.'''

        data = []

        if request.GET['incoming'] == 'true':
            data = [
                {
                    'id': 1,
                    'client_name': 'John Smith',
                    'date_referred': '1/1/2017',
                    'referring_entity': 'St. Patrick Center',
                    'referring_to': 'your_org',
                    'referral_status': 'accepted',
                    'notes': [
                        {
                            'author': 'Sally Johnson',
                            'text': 'This man has been referred.',
                            'date': '1/1/2017'
                        }
                    ]
                },
                {
                    'id': 2,
                    'client_name': 'Jane Smith',
                    'date_referred': '1/1/2017',
                    'referring_entity': 'St. Patrick Center',
                    'referring_to': 'your_org',
                    'referral_status': 'accepted',
                    'notes': [
                        {
                            'author': 'Sally Johnson',
                            'text': 'This man has been referred.',
                            'date': '1/1/2017'
                        }
                    ]
                }
            ]
        else:
            data = []

        return json_response(data)

    @staticmethod
    def post(request):
        '''Create a new referral.'''

        return json_response()


class ReferralView(View):
    @staticmethod
    def get(request, referral_id):
        '''Retrieve single referral.'''

        return json_response()

    @staticmethod
    def post(request, referral_id):
        '''Update single referral.'''

        return json_response()
