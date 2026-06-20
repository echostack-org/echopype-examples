from pathlib import Path
import shutil
from zipfile import ZipFile

import pooch

EXAMPLE_DATA_DIR = Path("example_data")

DATASETS = {
    "ts_spectrum_example_data": {
        "release": "example-data-v1",
        "asset": "ts_spectrum_example_data.zip",
        "sha256": "dae603937d05d0d0a5dd41c90b9eafa3c540c95e0f6b298ceeddc7f23d163f4b",
        "files": [
            "IMR-D20211215-T143432-TSf.raw",
            "crimac_tsf_reference_outputs.npz",
        ],
    },
}

def fetch_dataset(name: str, data_dir: Path = EXAMPLE_DATA_DIR) -> Path:
    """Download and extract an example dataset if it is not available locally."""
    if name not in DATASETS:
        raise ValueError(f"Unknown dataset: {name}")

    dataset = DATASETS[name]
    dataset_dir = data_dir / name
    expected_files = [dataset_dir / file for file in dataset["files"]]
    expected_sha256 = dataset["sha256"]
    marker_file = dataset_dir / ".sha256"

    fetcher = pooch.create(
        path=data_dir,
        base_url=(
            "https://github.com/echostack-org/echopype-examples/"
            f"releases/download/{dataset['release']}/"
        ),
        registry={dataset["asset"]: f"sha256:{expected_sha256}"},
    )

    # This verifies the cached zip hash.
    # If the local zip is missing/stale/corrupted, Pooch redownloads it.
    zip_path = Path(fetcher.fetch(dataset["asset"]))

    local_extract_valid = (
        all(file.exists() for file in expected_files)
        and marker_file.exists()
        and marker_file.read_text().strip() == expected_sha256
    )

    if local_extract_valid:
        print(f"Using local dataset: {dataset_dir}")
        return dataset_dir

    print(f"Extracting dataset: {name}")

    if dataset_dir.exists():
        shutil.rmtree(dataset_dir)

    with ZipFile(zip_path) as zip_file:
        zip_file.extractall(data_dir)

    missing_files = [file for file in expected_files if not file.exists()]
    if missing_files:
        raise FileNotFoundError(
            "Dataset download/extraction finished, but some expected files are missing: "
            + ", ".join(str(file) for file in missing_files)
        )

    marker_file.write_text(expected_sha256 + "\n")

    return dataset_dir