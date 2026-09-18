conda env remove -n "csci2470" -y
conda env create -n "csci2470" -f env_setup/Other/csci2470.yml

## Install new environment.
conda run -n csci2470 python -m ipykernel install --user --name csci2470 --display-name "DL-F26 (3.11)"
