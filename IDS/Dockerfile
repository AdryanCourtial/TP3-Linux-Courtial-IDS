FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get install -y sudo && useradd ids && usermod -aG sudo ids 
RUN pip install -r requirements.txt 

USER ids

CMD [ "sudo", "python3", "ids.py", "--init" ]

