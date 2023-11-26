# Python Design pattern

## What is \_\_init\_\_.py

It used to be a required part of a package (old, [pre-3.3](https://docs.python.org/3/reference/import.html#regular-packages) "regular package", not [newer 3.3+](https://docs.python.org/3/reference/import.html#namespace-packages) "namespace package").

## Example Inheritance Exception

BaseException \
+-- KeyboardInterrupt \
+-- Exception \
&nbsp;&nbsp;+-- ArithmeticError \
&nbsp;&nbsp;&nbsp;&nbsp;+-- ZeroDivisionError

## What is @property

To impose that is a protected instance. It's similar to {get;} in c#

## Type check with mypy

you can use `mypy` to do type checking. By the way, you need to provide type hint in the code.
