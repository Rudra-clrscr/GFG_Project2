$PROJECT_ID="gfgproject-495207"
$DATASET_NAME="mcp_bakery"
$BUCKET_NAME="gs://mcp-bakery-data-gfgproject-495207"

bq query --use_legacy_sql=false "CREATE OR REPLACE TABLE ${DATASET_NAME}.demographics ( zip_code STRING, city STRING, neighborhood STRING, total_population INT64, median_age FLOAT64, bachelors_degree_pct FLOAT64, foot_traffic_index FLOAT64 )"
bq load --source_format=CSV --skip_leading_rows=1 --ignore_unknown_values=true --replace "${PROJECT_ID}:${DATASET_NAME}.demographics" "$BUCKET_NAME/demographics.csv"

bq query --use_legacy_sql=false "CREATE OR REPLACE TABLE ${DATASET_NAME}.bakery_prices ( store_name STRING, product_type STRING, price FLOAT64, region STRING, is_organic BOOL )"
bq load --source_format=CSV --skip_leading_rows=1 --replace "${PROJECT_ID}:${DATASET_NAME}.bakery_prices" "$BUCKET_NAME/bakery_prices.csv"

bq query --use_legacy_sql=false "CREATE OR REPLACE TABLE ${DATASET_NAME}.sales_history_weekly ( week_start_date DATE, store_location STRING, product_type STRING, quantity_sold INT64, total_revenue FLOAT64 )"
bq load --source_format=CSV --skip_leading_rows=1 --replace "${PROJECT_ID}:${DATASET_NAME}.sales_history_weekly" "$BUCKET_NAME/sales_history_weekly.csv"

bq query --use_legacy_sql=false "CREATE OR REPLACE TABLE ${DATASET_NAME}.foot_traffic ( zip_code STRING, time_of_day STRING, foot_traffic_score FLOAT64 )"
bq load --source_format=CSV --skip_leading_rows=1 --replace "${PROJECT_ID}:${DATASET_NAME}.foot_traffic" "$BUCKET_NAME/foot_traffic.csv"
