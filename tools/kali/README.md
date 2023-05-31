# Kali in Docker

This Docker image is based on the [Kali Linux's](https://www.kali.org/) rolling distribution, and is intended to provide an environment with Kali Linux command-line tools readily available within a Docker container.

## Image Details

    - **Base Image:** kalilinux/kali-rolling:amd64
    - **Author:** [F.](https://github.com/hyp3rd)
    - **Description:** Kali CLI tools in Docker
    - **Source:** GitHub

### Environment Variables

    `DEBIAN_FRONTEND`: Set to noninteractive to prevent any interactive frontend interface from being used.
    `HOME`: Set to /home/kali to define the home directory.
    `DISPLAY`: Set to :1 to specify the X display to use.

### Installed Packages

This Docker image might include the following packages:

    ```text
    net-tools
    wget
    python3
    python3-pip
    unzip
    geany
    kali-linux-large
    seclists
    menu
    ```

After installing the necessary packages, the image also performs cleanup to reduce the size of the image.

### Usage

To use this Docker image, you will need Docker installed on your system. Then, you can pull this image from the Docker Hub or build it locally using Docker build command.

To build this image locally, save the [**Dockerfile**](./Dockerfile) to your system, navigate to the directory containing the Dockerfile, and run the following command:

    ```bash
    docker build -t kali-in-docker .
    ```

This command builds the Docker image and tags it as `kali-in-docker`.

**To run a container using this image, use the Docker run command:**

    ```bash
    docker run -it --rm kali-in-docker bash
    ```

This command runs the `kali-in-docker` image in a new container. The `-it` option starts the container in interactive mode, and the `--rm` option removes the container after it stops.

## Notes

The Dockerfile for this image is available on GitHub. You can modify it to suit your needs.

Please note that the `kali-linux-large` package includes a large number of penetration testing tools, and the image size will be considerably large. If you need a smaller image, consider using `kali-linux-core` or `kali-linux-default` instead.

## Support

For any issues, comments, or suggestions, please open an issue in this GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for details.
