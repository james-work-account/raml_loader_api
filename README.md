# RAML Loader API

## Write RAML, export as JSON

### Requirements

- Requires python 3
- Install necessary packages through pip

### Usage

- Run with `python3 manage.py runserver`
- Hit with `GET http://localhost:8000/raml/<RAML_FOLDER_NAME>`
- e.g: http://localhost:8000/raml/example
- To make a new API document, it must be named `application.raml` and be placed in its own folder within the `raml` directory. For example, `/raml/example/application.raml`.

### Note

This actually uses the Python YAML loader and PyYaml to work so will work with YAML and RAML files, as long as the `*.raml` files conform to YAML specs.
