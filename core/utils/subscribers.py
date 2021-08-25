from core.forms import SubscribeForm


def subscribe(request):
    return {'subscribe_form': SubscribeForm()}
