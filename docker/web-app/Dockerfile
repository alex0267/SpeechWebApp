FROM node:15.5.0-alpine3.12 AS base
WORKDIR /app
COPY web-app .
RUN rm -rf node_modules
RUN npm install
RUN npm run build-css
RUN npm run build-js
COPY web-app/css/fonts static/fonts
COPY web-app/img/*.png static/img/

FROM python:3.9-slim AS build
WORKDIR /app
COPY --from=0 /app .
RUN apt update && apt --yes install build-essential
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["uwsgi", "--socket", "0.0.0.0:3000", "--protocol=http", "-w", "wsgi:app"]
