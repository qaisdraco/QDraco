# tests/test_input_validator.py

import unittest
from QDraco import InputValidator

class TestInputValidator(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.validator = InputValidator()

    def test_path_traversal(self):
        """Test detection of path traversal patterns."""
        path_traversals = [
            "../../etc/passwd",  # يجب اكتشافه
            "..%2F..%2F..%2Fetc%2Fpasswd",  # تصفح مسارات مشفر في URL
            "C:\\Windows\\System32",  # تصفح مسارات بأسلوب Windows
            "C:\\Windows\\..\\System32",  # مسار بترميز معقد
            "Hello World"  # لا ينبغي اكتشافه
        ]

        results = [self.validator.validate_path_traversal(input_str) for input_str in path_traversals]
        
        for input_str, result in zip(path_traversals, results):
            print(f"Input: {input_str}, Result: {result}")

        self.assertFalse(results[0])  # يجب أن تكون False لتصنيفها كمدخلات غير صالحة
        self.assertFalse(results[1])  # يجب أن تكون False لتصنيفها كمدخلات غير صالحة
        self.assertFalse(results[2])  # يجب أن تكون False لتصنيفها كمدخلات غير صالحة
        self.assertFalse(results[3])  # يجب أن تكون False لتصنيفها كمدخلات غير صالحة
        self.assertTrue(results[4])   # يجب أن تكون True للمدخلات التي لا تحتوي على تصفح مسارات

if __name__ == "__main__":
    unittest.main()
