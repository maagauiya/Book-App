from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import get_authorization_header
from rest_framework import authentication, exceptions

from apps.user.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or len(auth) != 2:
            return None

        try:
            from apps.user.register.utils import verify_token

            token = auth[1].decode()
            payload = verify_token(token)

            if not payload:
                raise exceptions.AuthenticationFailed(_('Invalid token.'))

        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(payload)

    def authenticate_credentials(self, payload):
        user_id = payload.get('user_id')

        if not user_id:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        try:
            user = User.objects.get(id=user_id)

            if not user.is_active:
                raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

            return user, None

        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Invalid token.'))
