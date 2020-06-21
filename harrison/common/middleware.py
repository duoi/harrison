from access_logs.models import Event

def RequestLoggingMiddleware(get_response):
    """
    Log all events, even by unauthenticated users.

    Stores the user, the url, and the headers as a json dump.

    :param get_response:
    :return:
    """
    def middleware(request):
        params = {
            'user': request.user if request.user.is_authenticated else None,
            'url': request.path,
            'request_dump': request.headers
        }
        Event.objects.create(**params)

        response = get_response(request)

        return response

    return middleware
