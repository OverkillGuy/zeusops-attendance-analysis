# ZeusOps Attendance Analysis

Data analysis on the Zeusops ArmA unit attendance sheet

Requires Python 3.10


## Usage

Generate the database from attendance CSV, then visualize it as a local website

### Run the command

Install the dependencies first:

    make install
    # or
	poetry install

Download the Attendance sheet as CSV from Google Docs, save it as
`attendance.csv` then run it through the scripts provided:

    make serve
    # aka
    zeusops-attendance-analysis attendance.csv attendance.db

This generates an sqlite database of our attendance sheet, which can be
visualized via: 

    poetry run datasette -i attendance
    # aka
    make serve

Then inside the virtual environment, launch the command:

    # Run single command inside virtualenv
    poetry run zeusops-attendance-analysis attendance.csv attendance.db

    # or
    # Load the virtualenv first
    poetry shell
    # Then launch the command, staying in virtualenv
    zeusops-attendance-analysis attendance.csv attendance.db
    

## Development

### Python setup

This repository uses Python3.10, using
[Poetry](https://python-poetry.org) as package manager to define a
Python package inside `src/zeusops_attendance_analysis/`.

`poetry` will create virtual environments if needed, fetch
dependencies, and install them for development.


For ease of development, a `Makefile` is provided, use it like this:

	make  # equivalent to "make all" = install lint docs test build
	# run only specific tasks:
	make install
	make lint
	make test
	# Combine tasks:
	make install test

Once installed, the module's code can now be reached through running
Python in Poetry:

	$ poetry run python
	>>> from zeusops_attendance_analysis import main
	>>> main("blabla")


This codebase uses [pre-commit](https://pre-commit.com) to run linting
tools like `flake8`. Use `pre-commit install` to install git
pre-commit hooks to force running these checks before any code can be
committed, use `make lint` to run these manually. Testing is provided
by `pytest` separately in `make test`.

### Documentation

Documentation is generated via [Sphinx](https://www.sphinx-doc.org/en/master/),
using the cool [myst_parser](https://myst-parser.readthedocs.io/en/latest/)
plugin to support Markdown files like this one.

Other Sphinx plugins provide extra documentation features, like the recent
[AutoAPI](https://sphinx-autoapi.readthedocs.io/en/latest/index.html) to
generate API reference without headaches.

To build the documentation, run

    # Requires the project dependencies provided by "make install"
    make docs
	# Generates docs/build/html/

To browse the website version of the documentation you just built, run:

    make docs-serve

And remember that `make` supports multiple targets, so you can generate the
documentation and serve it:

    make docs docs-serve


### Templated

This repo is templated, using commit hash: `f596a46e4abf80e84e659353d5daaf54c5d01d78`


## TODO list

This code is obviously not done. The following are improvements I'll be
considering soon:
- Merging data from `#attendance` channel (for reducing error rates)
- Adding a table for roles to separate the junk-y ones ("PRESENT") from the T1s etc
- Enhance operations data by injecting `#events-briefing` data
- Add the info from the `#events` bot to the operations
