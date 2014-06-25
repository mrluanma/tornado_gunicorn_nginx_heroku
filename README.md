tornado_gunicorn_nginx_heroku
=============================

Manage a bunch of Tornado app processes on one Heroku dyno with
[Gunicorn](http://gunicorn.org/).

```bash
$ heroku create --buildpack https://github.com/ddollar/heroku-buildpack-multi.git
$ git push heroku master
$ heroku open
```
