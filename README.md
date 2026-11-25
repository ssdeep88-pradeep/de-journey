# de-journey

My step-by-step path into data engineering, one week at a time.

## Week 1 – CSV profiling + Docker

| File | What it does |
|------|--------------|
| `week01/csv_profile.py` | Profiles a CSV using only the standard library (types, nulls, uniques, min/max, duplicate rows) |
| `week01/pandas_profile.py` | Same profile using pandas |
| `week01/Dockerfile` | Image for the standard-library version |
| `week01/Dockerfile.pandas` | Image for the pandas version, ordered so the pip install layer is cached |

### Run it

```powershell
cd week01
docker build -t csv-profile .
docker run --rm -v "${PWD}:/data" csv-profile /data/sample.csv

docker build -f Dockerfile.pandas -t csv-profile-pandas .
docker run --rm -v "${PWD}:/data" csv-profile-pandas /data/sample.csv
```

### What I learned
- Git branches + pull requests
- Docker images, containers, and volume mounts (`-v`)
- Layer caching: copy `requirements.txt` and install before copying code
- pandas turns int columns with blanks into float
