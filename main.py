import FirebaseAdmin
import pprint

if __name__ == '__main__':
    print(FirebaseAdmin.app)
    new_user = FirebaseAdmin.new_user('ddsddsdfa34@gmail.com', '1Bemigbar1!tr#ythAA')
    print(f"Firebase successfully created a new user with email - {new_user.email} and user id - {new_user.uid}")
    pprint.pprint(FirebaseAdmin.sign_in_with_email_and_password('ddsddsdfa34@gmail.com', '1Bemigbar1!tr#ythAA'))




