install:
	poetry install


build:
	poetry build


gendiff:
	poetry run gendiff


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl


package-uninstall:
	python3 -m pip uninstall dist/*.whl