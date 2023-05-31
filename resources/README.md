# Resources

In this directory, you can find the resources used in this project. To avoid cloning `seclists` or `fuzzdb` repositories, the files needed from these repositories are included in this directory.

**Most importantly**, there's a full-fledged breakdown of the infamous [OWASP crAPI project](./crAPI/README.md), a vulnerable API that can be used to learn about API security.

## seclists

The `seclists` repository contains multiple types of lists used during security assessments. Here are gathered the lists used in this project:

- `fuzzing/4-digits-0000-9999.txt`: This list contains all the 4-digit numbers from 0000 to 9999.
- `fuzzing/SQLi/Generic-SQLi.txt`: This list contains generic SQL injection payloads.
- `fuzzing/SQLi/Generic-NoSQLi.txt`: I've crafted this list containing generic NoSQL injection payloads.
