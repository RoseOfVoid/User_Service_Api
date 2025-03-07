from .validation_functions import respond_missing_info


async def check_login_info(params: dict):
    requested_params = ['username', 'password']
    missing_info = []
    for info in requested_params:
        if info not in params.keys():
            missing_info.append(info)

    if missing_info:
        respond_missing_info(missing_info)
