#!/usr/bin/env bash
export VERSION=$(poetry run soh version)
python setup.py sdist bdist_wheel
twine upload dist/soh-${VERSION}*
git tag -a ${VERSION} -m "${VERSION}"
git push --tags