import os
import requests
import itertools
from zipfile import ZipFile

# Data source: https://www.nber.org/research/data/current-population-survey-cps-basic-monthly-data

# Create directories if they don't exist
os.makedirs("data/CPS_from_1989/zips", exist_ok=True)

# Access to 2021 and 2022 zip files (some?) are forbidden, probably due to the server issue.
# Hence separate procedure for 2021 and 2022 data.
years_zip = [str(year) for year in list(range(1989, 2021)) + list(range(2023, 2025))]
years_2122 = [str(year) for year in range(2021, 2023)]
months = [f"{month:02d}" for month in range(1, 13)]

yms_zip = list(itertools.product(years_zip, months))
# Remove July 2024 and later as not available.
yms_zip = list(filter(lambda x: not (x[0] == '2024' and int(x[1]) >= 7), yms_zip))
yms_2122 = itertools.product(years_2122, months)

urls_zip = [f"https://data.nber.org/cps-basic3/dta/{ym[0]}/cpsb{ym[0]}{ym[1]}_dta.zip" for ym in yms_zip]
destfiles_zip = [f"data/CPS_from_1989/zips/cpsb{ym[0]}{ym[1]}_dta.zip" for ym in yms_zip]

urls_2122 = [f"https://data.nber.org/cps-basic3/dta/{ym[0]}/cpsb{ym[0]}{ym[1]}.dta" for ym in yms_2122]
destfiles_2122 = [f"data/CPS_from_1989/cpsb{ym[0]}{ym[1]}.dta" for ym in yms_2122]

# Download and unzip data except 2021 and 2022
# Download size: 4.09GB
# Extracted size: 28.4GB
for (url, destfile) in zip(urls_zip, destfiles_zip):
    print(f"Downloading {url}")
    response = requests.get(url)
    with open(destfile, 'wb') as f:
        f.write(response.content)
    print(f"Extracting {destfile}")
    with ZipFile(destfile, 'r') as zip_ref:
        zip_ref.extractall("data/CPS_from_1989")

# Download dta from 2021 and 2022
# Download size: 1.53GB
for (url, destfile) in zip(urls_2122, destfiles_2122):
    print(f"Downloading {url}")
    response = requests.get(url)
    with open(destfile, 'wb') as f:
        f.write(response.content)