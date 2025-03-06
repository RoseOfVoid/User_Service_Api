from utils import check_requested_info, respond_missing_info,check_duplicity, check_email_validity

from fastapi import APIRouter, Request, HTTPException

router = APIRouter()


@router.post("/register")
def register_user(request: Request):
    params = dict(request.query_params)
    missing_params = check_requested_info(params)
    if missing_params:
        return respond_missing_info(missing_params)
    if not check_email_validity(params['email']):
        return HTTPException(status_code=400, detail="Invalid email")
    if check_duplicity(params):
        return HTTPException(status_code=400, detail="User already exists")
    return {"Success": f"User Created with username {params['username']} created"}
