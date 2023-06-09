import pytest
from dbt.tests.util import run_dbt

# our file contents
from tests.functional.fixtures import (
    my_seed_csv,
    my_model_sql,
    schema_yml
)

# class must begin with 'Test'
class TestExample:
    """
    Methods in this class will be of two types:
    1. Fixtures defining the dbt "project" for this test case.
       These are scoped to the class, and reused for all tests in the class.
    2. Actual tests, whose names begin with 'test_'.
       These define sequences of dbt commands and 'assert' statements.
    """
    
    # configuration in dbt_project.yml
    @pytest.fixture(scope="class")
    def project_config_update(self):
        return {
          "name": "example",
          "models": {"+materialized": "view"}
        }

    # everything that goes in the "seeds" directory
    @pytest.fixture(scope="class")
    def seeds(self):
        return {
            "my_seed.csv": my_seed_csv,
        }

    # everything that goes in the "models" directory
    @pytest.fixture(scope="class")
    def models(self):
        return {
            "my_model.sql": my_model_sql,
            "my_model.yml": schema_yml,
        }
        
    # continues below
    def test_run_seed_test(self):
        """
        test to check the assertion results
        """
        # seed seeds
        results = run_dbt(["seed"])
        assert len(results) == 4
        # run models
        results = run_dbt(["run"])
        assert len(results) == 8
        # test tests
        results = run_dbt(["test"], expect_pass = True)
        assert len(results) == 25
        

