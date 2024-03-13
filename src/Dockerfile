FROM opensciencegrid/software-base:23-el9-release
RUN dnf install -y python3.11 python3-gfal2-util gfal2-plugin-gridftp cronie
RUN export ENABLE_SHA1=1
COPY src/gracc-backup.py /app/
WORKDIR /app
RUN touch /var/log/cron.log
RUN (crontab -l ; echo "0 * * * * python3.11 -u /app/gracc-backup.py ps-itb  &>> /var/log/cron.log") | crontab
RUN (crontab -l ; echo "0 * * * * python3.11 -u /app/gracc-backup.py ps-prod  &>> /var/log/cron.log") | crontab
RUN (crontab -l ; echo "0 * * * * python3.11 -u /app/gracc-backup.py raw  &>> /var/log/cron.log") | crontab
RUN (crontab -l ; echo "0 * * * * python3.11 -u /app/gracc-backup.py transfers  &>> /var/log/cron.log") | crontab
CMD crond & tail -f /var/log/cron.log