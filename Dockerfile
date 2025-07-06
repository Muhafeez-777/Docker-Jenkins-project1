FROM redhat/ubi8

RUN yum install -y python3 python3-pip && pip3 install flask pytest

COPY first.py /first.py
COPY test_app.py /test_app.py

CMD ["python3","/first.py"]


