echo [$(data)]: "START"

echo [$(data)]: "creating env with python 3.8 version"

conda create --prefix ./env python=3.8 -y

echo [$(data)]:- "activating the environment"

source activate ./env

echo[$(data)]: "installing the dev requirements"

pip install -r requirements.txt

echo [$(data)]:- "END"