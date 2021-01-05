FROM node:13.12.0-alpine

MAINTAINER aferszterowski@wewyse.com

COPY package*.json ./
COPY web-app .

RUN npm install \
    npm run build

EXPOSE 3000

CMD [ "npm", "run", "server"]
