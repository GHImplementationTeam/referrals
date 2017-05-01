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
                        'client_name': 'Ivory Jackson',
                        'date_referred': '1/15/2017',
                        'referring_entity': 'St. Patrick Center',
                        'referring_to': 'your_org',
                        'referral_status': 'arrived',
                        'notes': [
                            {
                                'author': 'Jessica Lister',
                                'text': 'This man has been referred.',
                                'date': '1/15/2017'
                            },
                            {
                                'author': 'Jessica Lister',
                                'text': 'Referral completed.',
                                'date': '1/15/2017'
                            }
                        ]
                    },
                    {
                        'id': 2,
                        'client_name': 'Matthew Pannakuk',
                        'date_referred': '1/18/2017',
                        'referring_entity': 'Sts Peter and Paul',
                        'referring_to': 'your_org',
                        'referral_status': 'accepted',
                        'notes': [
                            {
                                'author': 'Sally Johnson',
                                'text': 'This man has been referred.',
                                'date': '1/18/2017'
                            }
                        ]
                    },
                    {
                        'id': 3,
                        'client_name': 'John Drake',
                        'date_referred': '2/2/2017',
                        'referring_entity': 'Sts Peter and Paul',
                        'referring_to': 'your_org',
                        'referral_status': 'denied',
                        'notes': [
                            {
                                'author': 'Sally Johnson',
                                'text': 'This man has been referred.',
                                'date': '2/2/2017'
                            }
                        ]
                    },
                    {
                        'id': 4,
                        'client_name': 'Vincent Samuels',
                        'date_referred': '2/12/2017',
                        'referring_entity': 'Covenant House',
                        'referring_to': 'your_org',
                        'referral_status': 'completed',
                        'notes': [
                            {
                                'author': 'Ben Champion',
                                'text': 'This man has been referred.',
                                'date': '2/12/2017'
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
