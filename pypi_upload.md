# Updating rdflib-pyld-compat on PyPI

Notes to remind @zimeon...

## Updating <https://pypi.python.org/pypi/rdflib-pyld-compat>

  0. Merge tested changes into master and push to github
  1. Check `CHANGES.md` and version matches `rdflib-pyld-compat/__init__.py`
  2. Re-check all tests good (`python setup.py test` & travis)
  3. Check branches are as expected (git branch -a)
  4. Upload `python setup.py sdist upload`
  5. Check on PyPI at <https://pypi.python.org/pypi/rdflib-pyld-compat>
  6. Check install with `pip install rdflib-pyld-compat`
  7. Finally, back on working branch bump version in `rdflib-pyld-compat/__init__.py` and `CHANGES.md`
