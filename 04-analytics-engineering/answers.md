# Pre-requisites

Install DBT following course instructions.

Create ~/.dbt/profiles.yml with general configurations.

Copy `./taxi_rides_ny` from course repository (commands below will run from this directory).

Run ingestion script to get taxi data from 2019-2020.

Run `dbt debug` to test connection.

Run `dbt deps` to install dbt packages (it creates `./dbt_packages` directory).

Run `dbt build --target prod` to create all models and run tests.

# Question 1

Answer: `int_trips_unioned` only, as we are using `--select`

# Question 2

Answer: dbt will fail the test, returning a non-zero exit code
