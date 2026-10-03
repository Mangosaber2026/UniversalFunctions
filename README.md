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

from UF.Validators import TypeValidate
from numbers import Real

TypeValidate(Real)(56)

The distribution name is UniversalFunctions, while the Python import package is UF.

## Package Structure

UniversalFunctions is organized into several foundational components:

### UF

The main package containing the core infrastructure and utilities.

### UF.Validators

Provides runtime validation utilities and validation classes for enforcing types, ranges, relationships, and other constraints.

#### Notable components include:

* ``TypeValidate``
* ``TupleValidate``
* ``LessThan``
* ``LessOrEqual``
* ``GreaterOrEqual``
* ``Positive``
* ``real_validate``
* ``str_validate``
* Callable validation utilities

The validation system also contains the Quantum Turtle Mechanics (QTM) validation infrastructure used for more structured runtime validation.

### Decorators

UniversalFunctions provides reusable decorator infrastructure, including decorator composition and class-level decorator utilities.

#### Notable components include:

* ``class_decorator``
* ``deco_superposition``
* ``cls_deco_superposition``
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

## Development

Clone the repository and install it in editable mode:

git clone https://github.com/Mangosaber2026/UniversalFunctions.git
cd UniversalFunctions
pip install -e .

Editable installation allows changes to the source code to be reflected immediately without reinstalling the package.

## License

UniversalFunctions is distributed under the terms of the license included in this repository.

## Author

Miah M. Sabiq

UniversalFunctions is developed as an independent Python package and serves as foundational infrastructure for larger projects within the author's software ecosystem.