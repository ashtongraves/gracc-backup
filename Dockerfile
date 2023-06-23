FROM opensciencegrid/software-base:3.6-el8-release
RUN dnf install -y python3.11 python3-gfal2-util gfal2-plugin-gridftp
ADD test-resources/etc /etc
ADD test-resources/var /var
WORKDIR /script
COPY ./gracc-backup.py .
ENTRYPOINT ["python3.11", "./gracc-backup.py"]