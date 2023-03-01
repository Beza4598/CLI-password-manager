import FirebaseAdmin

if __name__ == '__main__':
    print(FirebaseAdmin.app)
    new_user = FirebaseAdmin.create_user('temp@gmail.com', None)
    print(f"Firebase successfully created a new user with email - {new_user.email} and user id - {new_user.uid}")




