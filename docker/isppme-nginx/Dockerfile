FROM node:14-buster-slim

COPY install_app.sh /install_app

RUN apt-get update && apt-get install git -y
RUN chmod +x /install_app
RUN /install_app isppme https://github.com/kingraphaii/isppme.git main

FROM frappe/erpnext-nginx:v13.9.2

COPY --from=0 /home/frappe/frappe-bench/sites/ /var/www/html/
COPY --from=0 /rsync /rsync
RUN echo -n "\nisppme" >> /var/www/html/apps.txt

VOLUME [ "/assets" ]

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
