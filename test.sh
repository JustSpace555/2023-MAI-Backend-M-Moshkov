#!bin/bash

ab -n 1000 -c 100 http://localhost:80/
wrk -t 4 -c 100 -d 10s http://localhost:9000/