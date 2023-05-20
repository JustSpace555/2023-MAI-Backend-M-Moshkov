FROM nginx:1.22.1

COPY nginx_docker.conf /etc/nginx/conf.d/default.conf
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 81
#RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf
#COPY nginx_docker.conf /etc/nginx/nginx.conf
#COPY default_docker.conf /etc/nginx/conf.d/default.conf