# OWASP API Security Project

## Synopsis

**The OWASP API Security Project** is a collaborative effort that aims to assist organizations, developers, and security professionals understand how to create, deploy, and maintain secure APIs. The project offers resources such as tools, documentation, and best practices to help individuals improve their API security posture.

This repository is a centralized location for all project-related materials, including documentation, tools, and other resources for developers and security experts to navigate the project's broad scope. The project's source code and tools aim to provide a reference to vulnerabilities, exploits, and defences for API security, while its documentation connects to best practices and guidelines.

**Please note** that the project is for **educational purposes only**, and users **should proceed at their own risk**.
The examples developed in the project are not intended for production use. **They purposely contain vulnerabilities and insecure configurations to demonstrate the risks associated with APIs.**

## Table of Contents

- [OWASP API Security Project](#owasp-api-security-project)
  - [Synopsis](#synopsis)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Tools](#tools)
    - [Documentation](#documentation)
    - [Resources](#resources)
      - [crAPI](#crapi)
      - [seclists](#seclists)
    - [docs](./docs/README.md)
      - [Burp Suite](./docs/burp.md)
      - [OWASP ZAP](./docs/zap.md)
      - [ffuf](./docs/ffuf.md)
      - [OWASP API Security Top 10 2023RC](./docs/README.md#owasp-api-security)
        - [0x01 Broken Object Level Authorization](./docs/README.md#0x01-broken-object-level-authorization)
        - [0x02 Broken User Authentication](./docs/README.md#0x02-broken-authentication)
        - [#0x03-broken-object-property-level-authorization](./docs/README.md#0x03-broken-object-property-level-authorization)
        - [0x04 Unrestricted Resource Consumption](./docs/README.md#0x04-unrestricted-resource-consumption)
        - [0x05 Broken Function Level Authorization](./docs/README.md#0x05-broken-function-level-authorization)
        - [0x06 Server-Side Request Forgery](./docs/README.md#0x06-server-side-request-forgery)
        - [0x07 Security Misconfiguration](./docs/README.md#0x07-security-misconfiguration)
        - [0x08 Lack of Protection from Automated Threats](./docs/README.md#0x08-lack-of-protection-from-automated-threats)
        - [0x09 Improper Assets Management](./docs/README.md#0x09-improper-assets-management)
        - [0xaa Unsafe Consumption of APIs](./docs/README.md#0xaa-unsafe-consumption-of-apis)
  - [Contributing](#contributing)
  - [Support](#support)
  - [License](#license)

## Getting Started

### Prerequisites

To use the tools in this project, you will need the following:

- [Docker](https://www.docker.com/) - A containerization platform that allows you to package your application and all its dependencies into a standardized unit for software development.
- [Docker Compose](https://docs.docker.com/compose/) - A tool for defining and running multi-container Docker applications (**NOTE:** Compose V2 is already included with all currently supported versions of Docker Desktop).
- [Git](https://git-scm.com/) - A distributed version control system.
- [Python](https://www.python.org/) - A programming language that lets you work quickly and integrate systems more effectively.
- [Python PIP](https://pypi.org/project/pip/) - A package installer for Python.
- [Burp Suite](https://portswigger.net/burp) - A graphical tool for testing Web application security.
- [OWASP ZAP](https://www.zaproxy.org/) - A free, open-source penetration testing tool for finding vulnerabilities in Web applications (Optional).
- [ffuf](https://github.com/ffuf/ffuf) - A fast web fuzzer written in Go.
- [Postman](https://www.postman.com/) - A collaboration platform for API development.
- [Visual Studio Code](https://code.visualstudio.com/) - A code editor optimized for building and debugging modern Web and cloud applications (Optional).

### Installation

To run the tools in this project, you must install the prerequisites listed above.
Once the system is ready, you can clone this repository to your local system using the following command:

```bash
git clone https://github.com/hyp3rd/OWASP-API-Security.git
```

## Usage

### Tools

The tools in this project are available in the [tools](./tools) directory.
The tools are categorized into subdirectories based on their programming language or purpose.
For example, the [tools/python](./tools/Python) directory contains tools written in Python, while the [tools/kali](./tools/kali) folder includes a Docker distribution of Kali Linux.

## Resources

The resources to aid you navigate the API Scurity with this project are available in the [resources](./resources) folder.
There you'll find the following:

### crAPI

The [crAPI directory](./resources/crAPI/README.md) contains a full breakdown with examples and solutions.

### seclists

The [seclists directory](./resources/README.md) contains a collection of multiple types of lists used during security assessments.

### Documentation

You can find the documentation for the OWASP top 10 vulnerabilities and the reference guide for the code examples in the [docs](./docs) directory.

## Contributing

We appreciate your contributions and would love you to share them with us! Just keep in mind that we value constructive input. Please review our [contributing guidelines](./CONTRIBUTING.md) to learn more about contributing. Thank you.

## Support

If you need any help or have any doubts, don't hesitate to contact me through [Twitter](https://twitter.com/_googoomuck_/) or [LinkedIn](https://www.linkedin.com/in/francesco-cosentino/). I'll be happy to assist you.

## License

This project is licensed under the [MIT License](./LICENSE).
