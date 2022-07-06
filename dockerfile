FROM python:latest

LABEL Maintainer="etienne.henn@gmail.com"

ENV NUM=3 \
    URL="https://al.co.za"

WORKDIR /home

RUN pip install requests

COPY response_time.py ./

CMD ["python","./response_time.py"]
