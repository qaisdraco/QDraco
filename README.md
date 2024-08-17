# QDraco

QDraco is a Python library designed to validate user inputs against common security vulnerabilities. This library helps in preventing various types of attacks such as SQL Injection, Cross-Site Scripting (XSS), Command Injection, Path Traversal, and others. It is a valuable tool for developers looking to enhance the security of their applications by validating potentially malicious inputs.


## Features

SQL Injection Prevention: Detects and prevents SQL injection attempts.
XSS (Cross-Site Scripting) Prevention: Identifies and blocks XSS attack patterns.
Command Injection Prevention: Protects against shell command injections.
Path Traversal Prevention: Safeguards against attempts to access unauthorized files and directories.
Remote and Local File Inclusion (RFI/LFI) Prevention: Blocks attempts to include remote or local files.
Remote Code Execution (RCE) Prevention: Detects patterns that could lead to code execution on the server.
Open Redirect Prevention: Prevents open redirect attacks.
CSRF (Cross-Site Request Forgery) Prevention: Identifies potential CSRF attack vectors.





## Installation
To install QDraco, you can use pip:

```bash
pip install QDraco
```

### Usage


Here is an example of how to use QDraco to validate different types of user inputs:

```python
from QDraco import InputValidator

validator = InputValidator()

# Example inputs to validate
sql_input = "SELECT * FROM users WHERE id = 1"
xss_input = '<script>alert("XSS")</script>'
command_input = "rm -rf /"
path_input = "../../etc/passwd"
csrf_input = '<form action="submit.php" method="post"><input type="hidden" name="csrf_token" value="..."></form>'
rfi_input = "http://example.com/shell.txt"
lfi_input = "../../../../../etc/passwd"
rce_input = "system('ls');"
open_redirect_input = "window.location='http://evil.com';"

# Validate inputs
print("SQL Injection Safe:", validator.validate_sql_input(sql_input))
print("XSS Safe:", validator.validate_html_input(xss_input))
print("Command Injection Safe:", validator.validate_command_input(command_input))
print("Path Traversal Safe:", validator.validate_path_traversal(path_input))
print("CSRF Safe:", validator.validate_csrf_input(csrf_input))
print("RFI Safe:", validator.validate_rfi_input(rfi_input))
print("LFI Safe:", validator.validate_lfi_input(lfi_input))
print("RCE Safe:", validator.validate_rce_input(rce_input))
print("Open Redirect Safe:", validator.validate_open_redirect_input(open_redirect_input))

```


### License


This project is licensed under the MIT License. See the LICENSE file for more details.

### Contact

If you have any questions or feedback, please feel free to reach out.

### Contributing

Contributions to QDraco are welcome! Whether it's a bug report, new feature, correction, or any other type of contribution, please feel free to open an issue or submit a pull request on the GitHub repository.

