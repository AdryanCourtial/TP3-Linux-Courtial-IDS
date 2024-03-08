FROM rockylinux

RUN dnf upgrade -y && dnf install python3.9 -y && dnf install pip && pip install psutil && pip install flask

#INSTALL LIB PYTHON : psutil et flask