

from ..utils import Object


class AuthenticationCodeType(Object):
    """
    Provides information about the method by which an authentication code is delivered to the user

    No parameters required.
    """
    ID = "authenticationCodeType"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "AuthenticationCodeTypeSms or AuthenticationCodeTypeFlashCall or AuthenticationCodeTypeCall or AuthenticationCodeTypeTelegramMessage":
        if q.get("@type"):
            return Object.read(q)
        return AuthenticationCodeType()