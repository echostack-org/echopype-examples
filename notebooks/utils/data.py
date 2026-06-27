from pathlib import Path
import pooch

EXAMPLE_DATA_DIR = Path("example_data")

DATASETS = {
    "ts_spectrum_example_data": {
        "release": "example-data-v1",
        "asset": "ts_spectrum_example_data.zip",
        "sha256": "A35A1108DCFAFAE725D826FFA23EA2E111FDB420E7CE433E49E1797381BB6763",
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

    if all(file.exists() for file in expected_files):
        print(f"Using local dataset: {dataset_dir}")
        return dataset_dir

    print(f"Downloading dataset: {name}")

    fetcher = pooch.create(
        path=data_dir,
        base_url=(
            "https://github.com/echostack-org/echopype-examples/"
            f"releases/download/{dataset['release']}/"
        ),
        registry={
            dataset["asset"]: f"sha256:{dataset['sha256']}",
        },
    )

    zip_path = Path(
        fetcher.fetch(
            dataset["asset"],
            processor=pooch.Unzip(),
        )
    )

    zip_path.unlink(missing_ok=True)

    missing_files = [file for file in expected_files if not file.exists()]
    if missing_files:
        raise FileNotFoundError(
            "Dataset download/extraction finished, but some expected files "
            "are missing: "
            + ", ".join(str(file) for file in missing_files)
        )

    return dataset_dir