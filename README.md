# Unit testing 101 - Python

This is a basic introduction to unit testing in Python.
To learn the basics of testing you will implement the well known game _Fizz buzz_.

Depending on who you ask you will get different answers according the rules of this game.
The basic concept is that multiple persons are counting from 1 to n (most probably you won't reach n on a cozy evening with your friends but that's a different story).
Everyone increments the number of previous player and says either the number, _fizz_, _buzz_ or _fizzbuzz_ depending on some conditions.

For this introduction we will use the following rules:

- respond with _fizz_ if the number is dividable by 3
- respond with _buzz_ if the number is dividable by 5
- respond with _fizzbuzz_ if the number is dividable by 3 **and** 5

## Getting started

### Setup

For this introduction we will use `pytest` to run unit tests.
The repository contains a `Pipfile` which alread defines the dependency to `pytest`.
To be able to run the test you need:

* Python3
* pip
* [pipenv](https://github.com/pypa/pipenv)

To initialize the virtualenv and install the required libraries run the following snippet:

```bash
$> pipenv install -d
```

### Running the tests

As soon as the virtualenv is initialized and dependencies are installed you're good to go.
Executing the tests is as straight forward as it can be.
Just run **one** of the following two snippets:

```bash
$> pipenv run pytest
```

```bash
$> pipenv shell
$> pytest
```

The second one "activates" the virtualenv, meaning, the activation script of the virtualenv is executed which updates your `$PATH` variable to give you access to all libraries installed in the virtualenv.

## Iteration 1

In the first iteration you will implement the function `fizz_buzz` so that all given unit tests are running successfully.
Keep in mind that till now everything is allowed:

```py
def fizz_buzz(number):
    if number == 3:
        return 'fizz'
    return f"{number}"
```

is an absolutely valid solution to run the first unit test successfully.
Unit testing (and especially TDD) aims to find the easiest solution available to solve the given problem!

The implementation of the function `fizz_buzz` will evolve while you're fixing all failing test cases.

When all test cases are fixed you will probably want to add more test cases to cover some edge cases!

## Iteration 2

In the second iteration we will add some additional rules your implementation should also take care off:

- respond with _fizz_ if the number contains the digit 3
- respond with _buzz_ if the number contains the digit 5
- respond with _fizzbuzz_ if the number contains the digits 3 **and** 5

Start by writing corresponding test cases **first** and then change your implementation to fix the failing test cases.

## Iteration 3

In the third iteration we will create a special edition:

- instead of _fizz_ return _Rick_
- instead of _buzz_ return _Morty_
- instead of _fizzbuzz_ return _RickMorty_

_Note: special credits if you manage to return **Rick and Morty** instead of **RickMorty**._

Start by updating the tests **first** to check for the new terms and adjust your code to actually do whatever the tests are expecting it to do!

## Iteration 4

In the forth and last iteration we will change back to _fizz_, _buzz_ and _fizzbuzz_ but:

- return _fizz_ if the number is dividable by **2** or contains the digit **2**
- return _buzz_ if the number is dividable by **7** or contains the digit **7**

_Note: free coffee for the first one who thought of creating commits for each iteration and could therefor roll back to the commit before Rick and Morty._

And again, **first** update and extend your test suite and after that start working on the actual implementation.

## Conclusion

Writing the tests first is one of the key principles of Test-Driven Development (TDD).
By writing the tests first you'll focus on what you expect the code to do and, probably even more import, not to do.
Furthermore by keeping the solution as simple as possible to get the tests <span style="color: green;">"green"</span> you're actively protecting yourself against over-engineering.

You should have noticed that even bigger changes are way easier with a good test suite because you don't have to worry if you forgot an edge case as long as the tests are running, you're on a good way to a reliable solution.