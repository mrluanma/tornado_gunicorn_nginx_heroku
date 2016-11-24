tornado_gunicorn_nginx_heroku
=============================

Manage a bunch of Tornado app processes on one Heroku dyno with [Gunicorn](http://gunicorn.org/).

Just click the button
---------------------

[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/mrluanma/tornado_gunicorn_nginx_heroku)

Or hardcore mode
----------------

```bash
$ heroku create
$ heroku buildpacks:set heroku/python
$ heroku buildpacks:add https://github.com/ryandotsmith/nginx-buildpack.git
$ git push heroku master
$ heroku open
```
