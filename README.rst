china-stock
===========

~~~~~~~
Install
~~~~~~~

::

	$ pip install china-stock

~~~
Use
~~~

Import china-stock module:

::
    
    >>> import chinastock as cs

Get stock prices information on nearest trading day:

::

	>>> cs.get_stock_today('000001','SZ')