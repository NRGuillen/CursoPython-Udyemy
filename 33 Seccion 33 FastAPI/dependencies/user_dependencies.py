from services.user_service import ServiceUser


def get_user_service() -> ServiceUser:
    return ServiceUser()