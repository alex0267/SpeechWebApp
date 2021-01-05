# SpeechWebApp

## Git workflow

- feature branch : feature/feature_name
- bug fix : fix/bug_name
- test : test/test_name

## Docker

### Frontend

Build:

```sh
docker build -t speech-emotion-webapp/frontend -f docker/web-app/Dockerfile .
```

Run:

```sh
docker run -p 3000:3000 speech-emotion-webapp/frontend
```
