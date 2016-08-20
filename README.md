# django-photoblog [![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)
## Install
    git clone git@github.com:relekang/django-photoblog.git
    cd django-photoblog
    python setup.py install

#### Add photoblog to installed apps
    INSTALLED_APPS = (
        ...
        'photoblog',
    )

#### Add to urlspattern in urls.py
    url(r'^photos/', include('photoblog.urls')),

## Dependecies
* sorl-thumbnail


## This is work in progress
Check out the [todo](https://github.com/relekang/django-photoblog/blob/master/todo.md)-list or
add a issue with a feature or bug.
