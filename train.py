import mlflow

with mlflow.start_run():
    mlflow.log_param("epochs",10)
    mlflow.log_metric("accuracy",95)