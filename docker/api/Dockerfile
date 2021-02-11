FROM python:3.9-slim

ENV PORT=8081

MAINTAINER aferszterowski@wewyse.com

RUN apt-get update && apt-get install -y gnupg2 && apt-get install -y wget

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get -y update - && \
    apt-get -y install libpq-dev && \
    apt-get -y install postgresql-client-11

# Install requirements
COPY api/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Create working dir and move py files inside
RUN mkdir /home/app
COPY api/ /home/app/
RUN ["chmod", "+x", "/home/app/start.sh"]
RUN ["chmod", "+x", "/home/app/wait-for-postgres.sh"]

WORKDIR /home/app/

RUN ["python", "make_credentials.json"]

EXPOSE 8081

CMD ["/home/app/start.sh"]
