FROM python:alpine
RUN mkdir /var/lib/graccarchive
RUN mkdir /var/lib/graccarchive/raw
RUN mkdir /var/lib/graccarchive/raw/output
RUN mkdir /var/lib/graccarchive/raw/secondary
COPY ./gracc-archive-raw.toml /etc/graccarchive/config/gracc-archive-raw.toml
COPY ./graccarchive/gracc-hcc-gracc.unl.edu-2023-05-26.tar.gz /var/lib/graccarchive/raw/output/gracc-hcc-gracc.unl.edu-2023-05-26.tar.gz
COPY ./graccarchive/gracc-hcc-gracc.unl.edu-2023-06-02.tar.gz /var/lib/graccarchive/raw/output/gracc-hcc-gracc.unl.edu-2023-06-02.tar.gz
COPY ./graccarchive/gracc-hcc-gracc.unl.edu-2023-05-27.tar.gz /var/lib/graccarchive/raw/output/gracc-hcc-gracc.unl.edu-2023-05-27.tar.gz
WORKDIR /script
COPY ./gracc-backup.py .
ENTRYPOINT [ "python3", "./gracc-backup.py", "raw"]