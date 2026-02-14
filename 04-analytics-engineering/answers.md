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

# Question 3

Run 

```Bash
duckdb taxi_rides_ny.duckdb "SELECT COUNT(*) as record_count FROM prod.fct_monthly_zone_revenue;"
```

Answer: 12184

# Question 4

Run

```Bash
duckdb taxi_rides_ny.duckdb "SELECT pickup_zone, SUM(revenue_monthly_total_amount) as total_revenue_2020 FROM prod.fct_monthly_zone_revenue WHERE service_type = 'Green' AND EXTRACT(YEAR FROM revenue_month) = 2020 GROUP BY pickup_zone ORDER BY total_revenue_2020 DESC LIMIT 1;"
```

Answer: East Harlem North │ 1817429.150

# Question 5

Run

```Bash
duckdb taxi_rides_ny.duckdb "SELECT SUM(total_monthly_trips) as total_trips_october_2019 FROM prod.fct_monthly_zone_revenue WHERE service_type = 'Green' AND revenue_month = '2019-10-01';"
```

Answer: 384624
