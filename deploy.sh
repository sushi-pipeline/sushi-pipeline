cd sushi-pipeline
git pull origin main

rm -rf ~/airflow/dags

cp -r ~/sushi-pipeline/etl/airflow/dags ~/airflow/dags
cp -r ~/sushi-pipeline/module ~/airflow/dags