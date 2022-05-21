# Development Note

## Requirements

- setuptools
- twine
- build

## Build Python package

Note that if you make modifications to the snippet (under `src/bbutils/snippet`), you have
to compile it first. Otherwise, the old version of JavaScript at
`src/bbutils/static/extract_submission_file.js` will be used.

Run

```console
python -m build
```

## Compile TypeScript to JavaScript

`typescript` package is required and can be installed by running `yarn install`.

cd into `src/bbutils/snippet/extract_submission`, and run

```console
./node_modules/.bin/tsc
```

The result JavaScript file is configured to be place in `src/bbutils/static/`.

## Upload to PyPI

After the package is built (and after the TypeScript source is compiled; if necessary), we can upload
the artifact to PyPI by running

```console
twine upload --repository pypi dist/*
```

To upload to the PyPI test server, replace `pypi` with `testpypi`.

This step assumes that the appropriate `~/.pypirc` file exists.
