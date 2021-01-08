FROM node:15.5.0-alpine3.12

MAINTAINER aferszterowski@wewyse.com

COPY web-app .

RUN npm install
RUN npm run build-css
RUN npm run build-js

EXPOSE 3000

CMD [ "npm", "run", "server"]
