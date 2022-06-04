import getpass
import unittest,math
import argon2, binascii

class OperationsManager():

    def __init__(self, a: float, b: float, c: str, d: str) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        return self.a / self.b

class TestOperationsManager(unittest.TestCase):

    def setUp(self):
        self.op_man = OperationsManager(a=1, b=1, c="ja sam c", d="ja sam c")

    def test_assertIsResultNaN(self, msg=None):
        standardMsg = "Result is not NaN"

        if(self.op_man.b == 0):

            if not math.isnan(self.op_man.perform_division()):
                self.fail(self._formatMessage(msg, standardMsg))

    def test_assertIsResultEqual(self, msg=None):
        standardMsg = "Result is not equal"

        if(self.op_man.c != self.op_man.d):
            self.fail(self._formatMessage(msg, standardMsg))


if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")

    argon2Hasher = argon2.PasswordHasher(time_cost=16, memory_cost=2**15, parallelism=2, hash_len=32, salt_len=16)
    hash = argon2Hasher.hash(password)

    if user != "root" or password != argon2Hasher.verify(hash, "123"):
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        a = float(input("A = "))
        b = float(input("B = "))
        ops_manager = OperationsManager(a, b)
        print(ops_manager.perform_division())

    unittest.main()

