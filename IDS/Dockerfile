FROM python3.9-bullseye

USER ids

RUN pip install --no-cache-dir -r requirements.txt

COPY . /opt

CMD [ "python3", "ids.py", "--init" ]

