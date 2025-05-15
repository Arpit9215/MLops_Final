import subprocess
import yaml
from pathlib import Path

# Directory where your versions are
DATASET_DIR = Path("data/raw")
VERSIONS = sorted(DATASET_DIR.glob("dataset_v*.csv"))

def update_params(dataset_path):
    version = dataset_path.stem.split("_")[-1]  # e.g., v1
    new_params = {
        'data': {
            'version': version,
            'raw_path': str(dataset_path),
            'processed_path': f"data_versions/{version}/processed.csv",
            'model_path': f"models/{version}/model.pkl"
        }
    }
    with open("params.yaml", "w") as f:
        yaml.dump(new_params, f)

def run_dvc():
    subprocess.run(["dvc", "repro"], check=True)

if __name__ == "__main__":
    for dataset_path in VERSIONS:
        print(f"\n🚀 Running pipeline for: {dataset_path.name}")
        update_params(dataset_path)
        run_dvc()
