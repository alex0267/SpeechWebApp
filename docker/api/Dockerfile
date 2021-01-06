FROM python:3.9-slim

MAINTAINER aferszterowski@wewyse.com

# Install requirements
COPY api/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# Create working dir and move py files inside
RUN mkdir /home/app
COPY api/ /home/app/
WORKDIR /home/app/

EXPOSE 8081

CMD ["python","-m", "src.app"]