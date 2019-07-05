# Jupyter Live Magic

A Jupyter Notebook %%magic for periodic auto re-run and refresh of Cells


Usage
------

Load extension inside a Jupyter notebook:

```
%load_ext jupyterlivemagic
```

Add code with Cell magic:

```
%%live
# code to re-run
```


Examples
--------

Display current time, update every second:

```
%%live
%%bash
date
```

Display current datetime, update every 500ms:

```
%%live --refresh-rate 500
import datetime
str(datetime.datetime.now())
```


Installation
------------

Install and activate dependencies:

- [ipywidgets](https://github.com/jupyter-widgets/ipywidgets)
- [jupyter-interval-widget](https://github.com/srizzo/jupyter-interval-widget)

Then:

    $ pip install jupyter-live-magic
