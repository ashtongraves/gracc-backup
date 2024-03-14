FROM opensciencegrid/software-base:23-el9-release
RUN dnf install -y python3.11 python3-gfal2-util gfal2-plugin-gridftp
COPY src/gracc-backup.py /app/
COPY src/crontab /etc/cron.d/
WORKDIR /app
RUN touch /var/log/cron.log
ENTRYPOINT ["tail", "-f", "/var/log/cron.log"]