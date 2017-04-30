from django.template.response import TemplateResponse
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def base_view(request):
    # if not request.user.is_authenticated():
    #     return TemplateResponse(request, 'base/404.html', {})

    return TemplateResponse(request, 'referrals.html', {})
