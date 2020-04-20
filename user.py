class Credentials:
    """
    Class that generates new instances of usersLogin.
    """

    userLogin_list = []

    def __init__(self,username,password,accountType):
        self.username = username
        self.password = password
        self.accountType = accountType

    def save_user_account(self):
        Credentials.userLogin_list.append(self)

    @classmethod
    def user_account_exists(cls,username):
        for user in cls.userLogin_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def display_user_accounts(cls):
        return cls.userLogin_list

    def delete_user_account(self):
        Credentials.userLogin_list.remove(self)

class Users:
    def __init__(self,login_username,login_password):
        self.login_username = login_username
        self.login_password = login_password