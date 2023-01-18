import unittest

from challenge1 import process_message


class TestChallenge1(unittest.TestCase):
    def test_noop(self):
        self.assertEqual(process_message("test"), "test", "No-op")

    def test_empty_paste(self):
        self.assertEqual(process_message("test[CTRL+V]"), "test", "Empty paste")

    def test_standalone_copy(self):
        self.assertEqual(process_message("test[CTRL+C]"), "test", "Standalone copy")

    def test_standalone_cut(self):
        self.assertEqual(process_message("test[CTRL+X]"), "", "Standalone cut")

    def test_first_cut(self):
        self.assertEqual(process_message("[CTRL+X]test"), "test", "First cut")

    def test_cut_paste(self):
        self.assertEqual(process_message("[CTRL+X]test[CTRL+V]"), "test", "Cut Paste")

    def test_cut_paste_2(self):
        self.assertEqual(process_message("test[CTRL+X][CTRL+V]"), "test", "Cut Paste 2")

    def test_cut_paste_paste(self):
        self.assertEqual(process_message("test[CTRL+X][CTRL+V][CTRL+V]"), "testtest", "Cut Paste Paste")

    def test_copy(self):
        self.assertEqual(process_message("test[CTRL+C][CTRL+V]"), "testtest", "Copy")

    def test_copy_paste_paste(self):
        self.assertEqual(process_message("test[CTRL+C][CTRL+V][CTRL+V]"), "testtesttest", "Copy paste paste")


if __name__ == '__main__':
    unittest.main()
