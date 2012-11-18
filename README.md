# django-photoblog
## Install
    git clone git@github.com:relekang/django-photoblog.git
    cd django-photoblog
    python setup.py install

    # add photoblog to installed apps
    INSTALLED_APPS = (
        ...
        'photoblog',
    )

    # add to urlspattern in urls.py
    url(r'^photos/', include('photoblog.urls')),


## This is work in progress
Check out the [todo](https://github.com/relekang/django-photoblog/blob/master/todo.md)-list or
add a issue with a feature or bug.