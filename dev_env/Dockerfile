# syntax=docker/dockerfile:1.4
FROM docker/dev-environments-default:stable-1 AS techno_build 

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-pip \
        python3-venv \
    && pip3 install --upgrade pip \
    && pip3 install poetry \
    && rm -rf /var/lib/apt/lists/*
