from django.conf.urls import url
import referrals

urlpatterns = [
    url(r'^referrals/$', referrals.ReferralsView.as_view()),
    url(r'^referral/(?P<referral_id>[-&\w]+)/$', referrals.ReferralView.as_view()),
]
