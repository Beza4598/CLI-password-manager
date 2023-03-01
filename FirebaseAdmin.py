import firebase_admin
from typing import Optional
from firebase_admin import auth
from firebase_admin.auth import UserRecord

app = firebase_admin.initialize_app()

def create_user(email: str, user_id: Optional[str]) -> UserRecord:
    return auth.create_user(email=email, uid=user_id) if user_id else auth.create_user(email=email)
