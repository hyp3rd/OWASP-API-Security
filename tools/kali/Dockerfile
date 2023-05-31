FROM kalilinux/kali-last-release

# Show off > Open Container Initiative (OCI) labels
LABEL org.opencontainers.image.authors="F." \
      org.opencontainers.image.description="Kali CLI tools in Docker" \
      org.opencontainers.image.source="https://github.com/hyp3rd/OWASP-API-Security/" \
      org.opencontainers.image.title="Kali in Docker"

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV HOME=/home/kali
ENV DISPLAY=:1

RUN echo "deb https://http.kali.org/kali kali-rolling main non-free contrib" > /etc/apt/sources.list && \
      echo "deb-src https://http.kali.org/kali kali-rolling main non-free contrib" >> /etc/apt/sources.list  && \ 
      apt-get update && apt-get install -y gnupg && \
      apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys 7D8D0BF6

# Update the system and install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
      net-tools \
      wget \
      python3 \
      python3-pip \
      unzip \
      kali-linux-headless \
      kali-system-cli \
      kali-tools-fuzzing \
      kali-tools-exploitation \
      kali-tools-sniffing-spoofing \
      kali-tools-web \
      kali-tools-database \
      kali-tools-passwords \
      kali-tools-top10 \
      seclists && \
      apt-get clean && \
      apt-get autoremove && \
      rm -rf /var/lib/apt/lists/*
