# Unit Testing Python Dynamic Code Execution
This is a demo of unit testing dynamic code execution with Python exec builtin function under some specific 
circumstances. In this project we have disallowed some builtin utilities to be used inside the dynamic code and allowed 
the usage of specific utilities from numpy and pandas libraries. Our objective is to observe and assert results from 
some specific kind of code execution where whitelisted and blacklisted utilities would be used.

## Prerequisites
Any Docker installation with optional compose utilities

## Run
Build an image and run removable containers from it
```shell script
docker image build -t unittesting_dynamic_code .
docker container run --rm -it unittesting_dynamic_code bash
sh run_test.sh
exit
``` 
Run docker compose commands
```shell script
docker-compose up
docker-compose down -v
```
