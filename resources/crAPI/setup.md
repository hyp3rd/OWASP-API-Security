# System setup

Here to follow a brief description of the system setup to get the project up and running and be able to execute the challenges.
The setup is friendly for both Linux and MacOS. Windows users are on their own. :P

## System requirements

- Docker
- [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload)
- [Ffuf](https://github.com/ffuf/ffuf)
- [Postman](https://www.postman.com/downloads/)
- curl

## Setup

1. Install [Docker](https://docs.docker.com/get-docker/)

2. Install `ffuf`

    ```bash
    brew install ffuf
    ```

3. Install [Postman](https://www.postman.com/downloads/)

4. Install [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload)

5. Download and install [Firefox](https://www.mozilla.org/en-US/firefox/new/)

The project is now ready to be used. It contains, among other things, the necessary files from [`seclists`](../seclists/) to execute the exploits in the project and the challenges against **crAPI**.

Additionally, you can install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) to execute [Kali Linux](https://www.kali.org/get-kali/) and [Burp Suite](https://portswigger.net/burp/communitydownload) in a virtual machine.

## Run crAPI

From the current directory run:

```bash
docker compose up -d
```

Remove the -d flag from the `docker compose up` command to see the logs flowing in the terminal.

You should be able to access the API at [http://localhost:8888](http://localhost:8888) and the mail server at [http://localhost:8025](http://localhost:8025).

**Pro-tip**, I have modified the `docker-compose.yml` to expose the ports on any interface `0.0.0.0`. Using your local IP address instead of `localhost` or `127.0.0.1` is preferable to avoid issues with the proxies setup.

## Caveats

The corporate laptops might get the morbs from the Cisco DNS proxy (heavy and massively sneaky) and Windows Defender (that detects a PHP reverse shell of all the files in the `seclists` repo).
