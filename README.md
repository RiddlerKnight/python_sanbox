# Python Design pattern

## What is \_\_init\_\_.py

It used to be a required part of a package (old, [pre-3.3](https://docs.python.org/3/reference/import.html#regular-packages) "regular package", not [newer 3.3+](https://docs.python.org/3/reference/import.html#namespace-packages) "namespace package").

## Example Inheritance Exception

BaseException \
+-- KeyboardInterrupt \
+-- Exception \
&nbsp;&nbsp;+-- ArithmeticError \
&nbsp;&nbsp;&nbsp;&nbsp;+-- ZeroDivisionError
