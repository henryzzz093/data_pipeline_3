project_dir := data_engineering
terraform_dir := ${project_dir}/infrastructure
mwaa_development_dir := ${project_dir}/mwaa_development
dev_docker := development/docker-compose.yaml


airflow-build:
	@ ./${mwaa_development_dir}/mwaa-local-env build-image

airflow-start:
	@ ./${mwaa_development_dir}/mwaa-local-env start

airflow-stop:
	@docker stop aws-mwaa-local-runner-202_local-runner_1
	@docker stop aws-mwaa-local-runner-202_postgres_1