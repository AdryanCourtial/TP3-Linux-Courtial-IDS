FROM python:3.9

WORKDIR /app

COPY . .

RUN useradd ids 
RUN pip install -r requirements.txt

USER ids

CMD [ "sudo", "python3", "ids.py", "--init" ]

