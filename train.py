import mlflow
import os

mlflow.set_tracking_uri("file:./mlruns")

with mlflow.start_run() as run:
    run_id = run.info.run_id
    print("Run ID:", run_id)

    # accuracy = 0.82  
    accuracy = 0.95  


    mlflow.log_metric("accuracy", accuracy)

    with open("model_info.txt", "w") as f:
        f.write(run_id + "\n")
        f.write(str(accuracy) + "\n")