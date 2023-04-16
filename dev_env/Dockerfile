# syntax=docker/dockerfile:1.4
FROM docker/dev-environments-default:stable-1 AS build_env

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-pip \
    && pip3 install --upgrade pip \
    && pip3 install poetry \
    && rm -rf /var/lib/apt/lists/*
