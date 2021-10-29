# Django Rest Framework Test Application

## Functional

- CRUD types of news
- CRUD news
- Possibility to get a list of all types of news
- Possibility to get a list of all news
- Possibility to get a list of news of a certain type

# Instructions

## Download repository

 ```
cd ~
it clone https://github.com/MelDxKviel/DjangoRFTest.git
cd DjangoRFTest
 ```

## Collect the image with the command:
```
docker build -t django_test_app .
```

## Launch image

```
docker run -p 8000:8000 django_test_app
```

Go to the url address: http://0.0.0.0:8000/ and enjoy the app :)

# API Documentation

List of all types of news -- /api/types

List of all news -- /api/articles

List of news by a certain type -- /api/articles/type/*type_id*

Certain article by id -- /api/articles/*article_id*

Certain type by id -- /api/types/*type_id*
