import datetime
from jose import jwt

from config.settings import settings
from models.auth import Token


def create_access_token_jwt(subjet: str): # subject = Identificador que representa al usuario en la app

    expires_in = datetime.datetime.now() + datetime.timedelta(minutes=int(settings.JWT_EXP_MINUTES))
    payload = {'sub': subjet,
               'exp': expires_in}
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token