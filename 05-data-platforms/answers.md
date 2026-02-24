# Pre-requisites

- Install Bruin CLI: `curl -LsSf https://getbruin.com/install/cli | sh`
- Initialize the zoomcamp template: `bruin init zoomcamp my-pipeline`
- Configure `.bruin.yml` with a DuckDB connection
- Implement the `materialize()` function in `assets/ingestion/trips.py`
- Add `connection: duckdb-default` to the asset definition
- Run `bruin validate ./pipeline/pipeline.yml` to ensure configuration is valid

# Question 1

**Answer:** `.bruin.yml` and `pipeline/` with `pipeline.yml` and `assets/`

Based on the project structure:
- `.bruin.yml` at the root defines environments and connections
- `pipeline/` directory contains the pipeline definition
- `pipeline.yml` defines the pipeline configuration (name, schedule, variables, etc.)
- `assets/` directory (inside pipeline/) contains the data assets (SQL, Python files)

# Question 2

**Answer:** `time_interval` - incremental based on a time column

It allows you to delete and re-insert data for a specific time period, which is ideal for reprocessing specific months of taxi data based on the `pickup_datetime` column.

# Question 3

**Answer:** `bruin run --var 'taxi_types=["yellow"]'`

Bruin seems to use `--var` flag to override pipeline variables. Since `taxi_types` is an array, it needs to be passed as a JSON array string in quotes.

# Question 4

**Answer:** `bruin run --select ingestion.trips+`

The `--select` flag with a `+` suffix runs the specified asset and all downstream dependencies. The syntax `ingestion.trips+` means "run ingestion.trips and everything that depends on it".

# Question 5

**Answer:** `name: not_null`

This is a standard data quality check in Bruin (and most data platforms like dbt).

# Question 6

**Answer:** `bruin lineage`

It generates and visualizes the dependency graph showing how assets relate to each other in the pipeline.

# Question 7

**Answer:** `--full-refresh`

It ensures that all tables are dropped and recreated from scratch, which is standard practice when running a pipeline for the first time or when you want to rebuild everything completely.
