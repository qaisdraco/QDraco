

import re
import logging
from .attack_patterns import AttackPatterns

class InputValidator:

    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def validate_path_traversal(self, user_input):
        """Validate path traversal patterns."""
        for pattern in AttackPatterns.PATH_PATTERNS:
            if re.search(pattern, user_input, re.IGNORECASE):
                logging.warning(f"Potential Path Traversal detected: {user_input}")
                return False
        return True


    def validate_html_input(self, user_input):
        for pattern in AttackPatterns.XSS_PATTERNS:
            if re.search(pattern, user_input):
                logging.warning(f"Potential XSS attack detected: {user_input}")
                return False
        return True

    def validate_command_input(self, user_input):
        for pattern in AttackPatterns.COMMAND_PATTERNS:
            if re.search(pattern, user_input):
                logging.warning(f"Potential Command Injection detected: {user_input}")
                return False
        return True

    def validate_path_traversal(self, user_input):
        for pattern in AttackPatterns.PATH_PATTERNS:
            if re.search(pattern, user_input):
                logging.warning(f"Potential Path Traversal detected: {user_input}")
                return False
        return True

    def validate_csrf_input(self, user_input):
        for pattern in AttackPatterns.CSRF_PATTERNS:
            if re.search(pattern, user_input):
                logging.warning(f"Potential CSRF attack detected: {user_input}")
                return False
        return True

    def validate_rfi_input(self, user_input):
        for pattern in AttackPatterns.RFI_PATTERNS:
            if re.search(pattern, user_input):
                logging.warning(f"Potential RFI attack detected: {user_input}")
                return False
        return True

    def validate_lfi_input(self, user_input):
        for pattern in AttackPatterns.LFI_PATTERNS:
            if re.search(pattern, user_input):
                logging.warning(f"Potential LFI attack detected: {user_input}")
                return False
        return True

    def validate_rce_input(self, user_input):
        for pattern in AttackPatterns.RCE_PATTERNS:
            if re.search(pattern, user_input):
                logging.warning(f"Potential RCE attack detected: {user_input}")
                return False
        return True

    def validate_open_redirect_input(self, user_input):
        for pattern in AttackPatterns.OPEN_REDIRECT_PATTERNS:
            if re.search(pattern, user_input):
                logging.warning(f"Potential Open Redirect detected: {user_input}")
                return False
        return True
