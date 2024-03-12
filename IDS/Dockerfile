FROM python:3.9

USER ids

RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt

CMD [ "python3", "ids.py", "--init" ]

