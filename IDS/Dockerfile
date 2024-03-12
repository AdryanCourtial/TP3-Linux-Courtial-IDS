FROM python:3.9


RUN useradd ids 
RUN pip install --no-cache-dir -r requirements.txt ,

USER ids

COPY . /opt

CMD [ "python3", "ids.py", "--init" ]

