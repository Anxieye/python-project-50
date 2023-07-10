install:
	poetry install


build:
	poetry build


lint:
	poetry run flake8 gendiff


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl


package-uninstall:
	python3 -m pip uninstall dist/*.whl


test:
	poetry run pytest


coverage:
	poetry run pytest --cov=gendiff --cov-report xml


selfcheck:
	poetry check


check: selfcheck test lint


