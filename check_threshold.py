import mlflow
import sys

with open("model_info.txt", "r") as f:
    lines = f.read().splitlines()

run_id = lines[0].strip()
accuracy = float(lines[1].strip()) 

print("Run ID:", run_id)
print("Accuracy:", accuracy)

if accuracy < 0.85:
    print("Model did NOT meet threshold")
    sys.exit(1)
else:
    print("Model passed threshold")