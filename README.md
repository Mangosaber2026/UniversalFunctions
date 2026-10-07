# UniversalFunctions

UniversalFunctions is a Python utility library providing foundational functions, validators, decorators, type utilities, and infrastructure for building structured Python applications and domain-specific APIs.

It is designed as an independent foundation layer that can be used on its own or as a dependency of larger projects such as GeometricalDomination.

## Installation

Install UniversalFunctions from PyPI:

```bash
pip install UniversalFunctions
```

The package requires Python 3.14 or later.

## Usage

UniversalFunctions is imported through the UF Python package:

```python
from UF.Validators import TypeValidate
from numbers import Real

TypeValidate(Real)(56)
```

The distribution name is UniversalFunctions, while the Python import package is UF.

## Package Structure

UniversalFunctions is organized into several foundational components:

### UF

The main package containing the core infrastructure and utilities.

### UF.Validators

Provides runtime validation utilities and validation classes for enforcing types, ranges, relationships, and other constraints.

#### Notable components include:

* ``TypeValidate`` -> class for validating an object against an expected type
* ``SequenceValidate`` -> class used to validate a sequence of objects
* ``LessThan`` -> class to validate a real number, constraint: value < expected
* ``qtm_validation_decorator`` -> when applied to a function, the decorator takes the provided parameter values and validates them against the expected type
* ``ErrorDedent``
* Callable validation utilities

This package inside UF contains numerous validators designed to validate all sorts of values and types, 
including some sophisticated ones like SequenceValidate which allows users to enter extra restrictions to the items in a given sequence.

There are 2 extra errors which are provided: 
* ``ItemCountError``
* ``ConstraintError``

ItemCountError was created since Python does not have an error for a situation where the values and types 
might be correct, though the number of items is not.

ConstraintError provides users to express that the type of a value might be correct, though it fails to pass a specific constraint.

The validation system also contains the Quantum Turtle Mechanics (QTM) validation infrastructure used for more structured runtime validation.

### Decorators

UniversalFunctions provides reusable decorator infrastructure, including decorator composition and class-level decorator utilities.

#### Notable components include:

* ``deco_superposition`` -> applies an arbitrary number of decorators to a function
* ``cls_deco_superposition`` -> applies an arbitrary number of decorators to every function in a class, except for protected ones (names starting with "_")
* Quantum Turtle Mechanics validation decorators

### Helper Functions

The library contains foundational helper functions intended to be reused by higher-level applications and APIs.

These utilities include mathematical and general-purpose functionality used throughout the surrounding ecosystem.

### Design Philosophy

UniversalFunctions exists as a foundational layer rather than as a standalone end-user application.

Its purpose is to provide reusable infrastructure that higher-level projects can build upon without duplicating common functionality.

The architecture separates foundational utilities from domain-specific functionality, allowing projects to depend on UniversalFunctions independently.

In the GeometricalDomination ecosystem, UniversalFunctions acts as the bridge between the underlying infrastructure and higher-level systems.

### Quantum Dimension

UniversalFunctions contains several architectural concepts inspired by the internal terminology of GeometricalDomination.

#### These include:

* Quantum Turtle Mechanics (QTM)
* Classical Turtle Mechanics (CTM)
* Quantum Turtle String Theory (QTST)
* The Quantum Dimension

These names describe architectural concepts within the project's validation and infrastructure systems.

## Requirements
Python 3.14 or later

UniversalFunctions is designed for modern Python and makes use of contemporary Python typing and language features.

## License

UniversalFunctions is distributed under the terms of the license included in this repository.

## Author

Miah M. Sabiq

UniversalFunctions is developed as an independent Python package and serves as foundational infrastructure for larger projects within the author's software ecosystem.