china-stock
===========

~~~~~~~
Install
~~~~~~~

	$ pip install china-stock

~~~~
Test
~~~~

	$ python -m unittest tests/test.py

~~~
Use
~~~

.. code:: python

	>>> from china_stock import Stock

	>>> symbol_list = ['sh000001', 'sh000002', 'sh601006']
	>>> stocks = Stock(symbol_list)

	>>> stock = stocks.get_data[0]