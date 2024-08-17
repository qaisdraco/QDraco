import re

class AttackPatterns:
    SQL_PATTERNS = [
        r"(?i)select.*from",  # SELECT statements
        r"(?i)union.*select",  # UNION SELECT statements
        r"(?i)insert.*into",  # INSERT statements
        r"(?i)drop.*table",  # DROP TABLE statements
        r"(?i)--",  # SQL comments
    ]

    XSS_PATTERNS = [
        r"<script.*?>.*?</script>",  # Script tags
        r"(?i)on\w+=['\"].*?['\"]",  # Inline event handlers
        r"javascript:.*",  # Javascript URIs
    ]

    COMMAND_PATTERNS = [
        r"(?:rm\s+-rf\s+/|:(){:|:};)",  # Dangerous command patterns
    ]
    PATH_PATTERNS = [
        r"\.\./",  # Unix-style path traversal
        r"\.\.\\",  # Windows-style path traversal
        r"%2F",  # URL encoded path separator
        r"%2e%2e%2f",  # URL encoded path traversal (e.g., ..%2F)
        r"%2e%2e\\",  # URL encoded path traversal (e.g., ..\)
        r"(\.\.\/)+",  # Multiple Unix-style path traversals
        r"(\.\.\\)+",  # Multiple Windows-style path traversals
        r"\/\.\.\/",  # Path traversal with additional slashes
        r"\\\.\.\\",  # Windows-style path traversal with additional slashes
        r"(?:%2e%2e%2f){2,}",  # Multiple encoded path traversals (e.g., ..%2F..%2F)
        r"(?:%2e%2e\\){2,}",  # Multiple encoded Windows-style path traversals
        r"(\.\.\/)+\.\.\/",  # Multiple traversals with end pattern
        r"(\.\.\\)+\.\.\\",  # Windows multiple traversals with end pattern
        r"[^\\\/]*\\\.\.\.\\[^\\\/]*",  # Windows-style traversal with intermediate directories
        r"[^\\\/]*\/\.\.\.\/[^\\\/]*",  # Unix-style traversal with intermediate directories
  
    ]
    CSRF_PATTERNS = [
        r"csrf_token",  # CSRF token checks
    ]

    RFI_PATTERNS = [
        r"http://",  # Remote File Inclusion
    ]

    LFI_PATTERNS = [
        r"\.\./",  # Local File Inclusion
    ]

    RCE_PATTERNS = [
        r"system\s*\(",  # Remote Code Execution
    ]

    OPEN_REDIRECT_PATTERNS = [
        r"window\.location",  # Open Redirect
    ]
