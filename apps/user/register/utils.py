import jwt
from datetime import datetime, timezone
from django.conf import settings


def verify_token(token, token_type='access'):
    """Verify the given token."""
    try:
        decoded_jwt = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
    except (jwt.exceptions.ExpiredSignatureError,
            jwt.exceptions.InvalidSignatureError,
            jwt.exceptions.DecodeError):
        return None

    if decoded_jwt['token_type'] != token_type:
        return None

    return decoded_jwt


def generate_token(user, exp_time, token_type='access'):
    """Generate a token for the given user."""
    expire_date = round((datetime.now(tz=timezone.utc) + exp_time).timestamp())

    body = {
        'token_type': token_type,
        'exp': expire_date,
        'user_id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    encoded_body = jwt.encode(
        body,
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )

    return encoded_body
