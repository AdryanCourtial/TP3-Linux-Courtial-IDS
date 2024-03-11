FROM rockylinux

RUN dnf upgrade -y && dnf install python3.9 -y && dnf install pip && pip install -r ./requirements.txt

COPY . ~

