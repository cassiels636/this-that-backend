from rest_framework import status
from rest_framework.response import Response


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        name = args[0].request.data.get("name", "")
        if not name:
            return Response(
                data={
                    "message": "Name is required to add this or that"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated
