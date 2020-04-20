import unittest
from user import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.newlogin = Credentials("kaphie","2001","putlocker")

    def test_init(self):
        self.assertEqual(self.newlogin.username,"kaphie")
        self.assertEqual(self.newlogin.password,"2001")
        self.assertEqual(self.newlogin.accountType,"putlocker")

    def test_save_user_account(self):
        self.newlogin.save_user_account()
        self.assertEqual(len(Credentials.userLogin_list),1)

    def tearDown(self):
        Credentials.userLogin_list = []

    def test_save_multiple_user_accounts(self):
        self.newlogin.save_user_account()
        test_user = Credentials("namesusing","passusing","accountusing")
        test_user.save_user_account()
        self.assertEqual(len(Credentials.userLogin_list),2)

    def test_user_accounts_exist(self):
        self.newlogin.save_user_account()
        test_user = Credentials("namesusing","passusing","accountusing")
        test_user.save_user_account()
        user_account_exists = Credentials.user_account_exists("namesusing")
        self.assertTrue(user_account_exists)

    def test_display_users_acounts(self):
        self.assertEqual(Credentials.display_user_accounts(),Credentials.userLogin_list)

    def test_delete_user_account(self):
        self.newlogin.save_user_account()
        test_user = Credentials("namesusing","passusing","accountusing")
        test_user.save_user_account()

        self.newlogin.delete_user_account()
        self.assertEqual(len(Credentials.userLogin_list),1)




if __name__ == '__main__':
    unittest.main()