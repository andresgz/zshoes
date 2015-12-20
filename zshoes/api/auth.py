from django.utils.translation import ugettext_lazy as _

from django.contrib.auth import get_user_model

from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed


class AuthenticationBasic(BasicAuthentication):
    def authenticate_credentials(self, userid, password):
        """
        Authenticate the userid and password against username and password.
        """
        User = get_user_model()
        user = User()
        if userid == 'my_user' and password == 'my_password':
            return (user, None)
        else:
            raise AuthenticationFailed(
                _('Invalid username/password.'))
