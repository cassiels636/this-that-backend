class ThisThatMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS, PUT, DELETE"
        response['Access-Control-Allow-Headers'] = "access-control-allow-origin"
        response['Access-Control-Expose-Headers'] = "access-control-allow-origin, access-control-allow-methods, " \
                                                    "access-control-allow-headers "
        response['Allow'] = "POST, GET, OPTIONS, PUT, DELETE"
        return response
