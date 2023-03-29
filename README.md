# dbt-tutorial

## How to setup and run the dbt:
1. Clone the repo and install requirements from requirements.txt
2. Setup the data in the seeds file:
For test data credit: https://github.com/dbt-labs/jaffle_shop
3. Run `dbt debug` on the git bash or console
4. Run `dbt seed ` to add data in target tables.
5. Run the models using `dbt run`
6. Test the models using `dbt test`
7. Generate documentation of the models `dbt docs generate`
8. Generate `dbt docs serve --port 5002` opens the documentations at specified port.

## How to test
1. Install pytest using `pip install pytest`
2. Run test using `python -m pytest tests/functional/test_example_failing.py -sv`
