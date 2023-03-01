import firebase_admin
from typing import Optional
from firebase_admin import auth
from firebase_admin.auth import UserRecord
import requests
import pprint
import json
import os

app = firebase_admin.initialize_app()
FIREBASE_WEB_API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")
rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"


def create_user(email: str, user_id: Optional[str]) -> UserRecord:
    return auth.create_user(email=email, uid=user_id) if user_id else auth.create_user(email=email)


def set_password(user_id: str, password: str) -> UserRecord:
    return auth.update_user(user_id, password=password)


def new_user(email:str, password: str) -> UserRecord:
    user_email: UserRecord = create_user(email, None)
    user: UserRecord = set_password(user_email.uid, password)
    return user


def sign_in_with_email_and_password(email: str, password: str, return_secure_token: bool = True):
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": return_secure_token
    })

    r = requests.post(rest_api_url,
                      params={"key": FIREBASE_WEB_API_KEY},
                      data=payload)

    return r.json()

