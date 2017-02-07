#!/bin/bash

echo "build image..."
docker build -t cr_api_dev:v1 .

echo "Run image ..."
docker run -p 80:80 -p 5000:5000 -d cr_api_dev:v1

echo "done!"

exit


