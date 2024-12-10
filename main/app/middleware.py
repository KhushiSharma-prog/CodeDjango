# your_app/middleware.py
import jwt
from django.conf import settings
from django.http import JsonResponse
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class JWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.headers.get('Authorization', None)

        if auth_header:
            try:
                # Extract token from the Authorization header
                token = auth_header.split(' ')[1]  # Bearer <token>
                payload = jwt.decode(token, settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=[settings.SIMPLE_JWT['ALGORITHM']])
                request.user_id = payload.get('user_id', None)
            except (IndexError, jwt.ExpiredSignatureError, jwt.InvalidTokenError) as e:
                return JsonResponse({"detail": "Invalid or expired token"}, status=401)

        # Proceed with the request if no token or token is valid
        response = self.get_response(request)
        return response
