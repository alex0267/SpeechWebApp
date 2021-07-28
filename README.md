# SpeechWebApp

SER: Speech Emotion Recognition

This is a web application which can record sample sentences voiced by different people acting on different emotions.


It can be split in four different blocks:

- the "frontend" which is a React application.
- the "backend" composed by three building blocks:
  - A posgresql database to record which emotion has been acted on a given sentence / time.
  - A google cloud bucket to record the actual sound file
  - An API that binds all together.

## Development and local considerations

### Git workflow

- feature branch : feature/feature_name
- bug fix : fix/bug_name
- test : test/test_name

### Docker

Build and start the web application together with the backend by typing from the root of the project:

```sh
docker-compose -f ./docker/docker-compose.yml -f ./docker/test.yml up
```

launch tests in docker 

```sh
docker-compose -f ./docker/docker-compose.yml -f/.docker/test.yml run backend pytest
```

### Local development without docker

#### Backend

Ensure that you have Postgres installed and running and issue the following commands to create a role and database:

```
$ psql postgres
postgres=# CREATE USER postgres WITH PASSWORD 'postgres';
postgres=# CREATE DATABASE test_db;
```

Installing the dependencies and running the server:

```sh
cd api/
python -m venv venv
pip install -r requirements.txt
source venv/bin/activate
PYTHONPATH=./ser_api POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres POSTGRES_DB=test_db POSTGRES_HOST=localhost POSTGRES_PORT=5432  python -m ser_api.app
```

If you have an empty sentences table in your database, you can populate it as follows:

```
$ psql test_db
postgres=# INSERT INTO sentence(sentence) VALUES('my sentence is the best');
postgres=# SELECT * FROM sentence;
 id |                    sentence                    
----|------------------------------------------------
  1 | my sentence is the best
```

#### Frontend

Installing the dependencies and running the webpack dev server:

```sh
cd web-app/
npm install
npm run start
```

## Deployment

The application is initially planned to be hosted on Google Cloud Platform.

Multiple elements has to be setup in order to deploy the application:

### Setting online database 

Google Cloud SQL databases can be setup using terraform (for more see [infra](./infra/README.md)).

Once the service started, the private IP addresses should be reported in the concerned deployment files (it can be obtained from the user interface on GCP):

- [Production deployment](./deployment/speech-webapp-single-deployment.yaml)
- [Development deployment](./deployment/speech-webapp-single-deployment-test.yaml)

Next, the historical data can be inserted into the database from the bucket `swa-sql-backup` on the `wewyse-centralesupelec-ftv` project using the web interface function to import the data.

### Setting frontend and backend deployment on kubernetes

The deployment is done based on two built docker images (one for frontend, one for backend) that can be found here [container registry](https://console.cloud.google.com/gcr/images/wewyse-centralesupelec-ftv/GLOBAL/speech-web-app-dev?project=wewyse-centralesupelec-ftv&authuser=0&gcrImageListsize=30).

The images can be build either locally with GCP cli or using GCP's Cloud Build which has the advantage of bulding and pushing the image to the container registry. The Cloud Build files are present in the `docker` subdirectory. Please refer to google documentation if you don't know how to use Cloud Build.

The last block of instructions can be found in the [deployment](./deployment/Readme.md) file.


## Shutting down the application

In order to shutdown the application one should :

- Export SQL data to `swa-sql-bucket` in SQL format to avoid any data loss.
- Stop the services, workload and cluster
- Delete generated secrets if any remaining
- Remove any related information from the registrar services (Cloud DNS etc.)
- Stop / delete the SQL instances
- DO NOT change / modify information saved in `swa-*` buckets
- Eventually cleanup the GCP registry.

You should be done.


### Note on user data loss

In the worse case scenario, the data from the first deployment has been exported for modelling
in [this bucket](wewyse-centralesupelec-ftv-data/raw_data), versions are tracked with dvc and more
information is available here : https://github.com/WeWyse/speech-emotion-recognition-modeling/tree/pytorch 