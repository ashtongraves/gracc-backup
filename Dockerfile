FROM opensciencegrid/software-base:3.6-el8-release
RUN yum install -y openssl-devel bzip2-devel libffi-devel wget
RUN yum groupinstall -y "Development Tools"
RUN wget https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tgz
RUN tar -xzvf Python-3.11.4.tgz -C /usr/src
RUN cd /usr/src/Python-3.11.4 && ./configure --enable-optimizations && make altinstall
RUN yum install -y python3-gfal2-util gfal2-plugin-gridftp
ADD test-resources/etc /etc
ADD test-resources/var /var
WORKDIR /script
COPY ./gracc-backup.py .
ENTRYPOINT ["python3.11", "./gracc-backup.py", "raw"]