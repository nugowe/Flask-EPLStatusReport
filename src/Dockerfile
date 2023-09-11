FROM ubuntu:latest

WORKDIR /opt

COPY . .

RUN apt-get update && apt-get -y install \
python3-pip python3 gunicorn lsof curl nginx supervisor && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

COPY nginx.conf /etc/nginx/nginx.conf

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod +x /opt/ReverseProxy-Start.sh

RUN mkdir -p /var/log/supervisord && touch /var/log/supervisord/supervisord.log 

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT supervisord -c /etc/supervisor/conf.d/supervisord.conf

EXPOSE 7878 80

