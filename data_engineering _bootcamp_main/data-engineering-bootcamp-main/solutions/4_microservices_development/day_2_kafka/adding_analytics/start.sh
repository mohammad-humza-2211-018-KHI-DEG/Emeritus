#!/bin/bash

docker-compose rm -svf  # Clean up previous instances
docker-compose up --build
