# SWE1 Django Polls App

[![Build Status](https://app.travis-ci.com/github/yatharthMogra/swe1-app.svg?branch=main)](https://app.travis-ci.com/github/yatharthMogra/swe1-app)
[![Coverage Status](https://coveralls.io/repos/github/yatharthMogra/swe1-app/badge.svg?branch=main)](https://coveralls.io/github/yatharthMogra/swe1-app?branch=main)

This repository contains the Django Polls application from tutorial parts 1-4, with CI/CD configured using Travis CI and deployment to AWS Elastic Beanstalk.

## Local Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## CI Checks

Travis runs these checks on push and pull requests:

- `black --check .`
- `flake8 .`
- `coverage run manage.py test`
- `coverage report`
- `coveralls` (after success)

## Deployment

On successful builds from `main`, Travis deploys to AWS Elastic Beanstalk (`django-polls-env`).

Deployed app URL:

- `https://django-polls-env.eba-mqvfbkhp.us-east-1.elasticbeanstalk.com/polls/`
