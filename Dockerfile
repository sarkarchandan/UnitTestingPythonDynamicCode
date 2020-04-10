FROM python:slim
RUN python3 -m pip install --user pandas==1.0.3
WORKDIR /src
COPY dynexec dynexec
COPY . .