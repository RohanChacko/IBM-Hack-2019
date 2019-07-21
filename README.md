# IBM-Hack-2019
## Topic: Energy Audit for households
#### Team: Greenticks
#### College: IIIT, Hyderabad
#### Deployed app: <https://energy-auditor.eu-gb.mybluemix.net>


## Contents

* [Installation](#installation)
* [Directory Structure](#directory-structure)
* [Implementation Details](#implementation-details)
* [Architecture](#architecture)
* [Notes](#notes)

## Installation
```bash
conda create --name venv
conda activate venv
# virtualenv --python=python3.6 venv
# source venv/bin/activate
pip install -r requirements.txt
```

## Run app locally

* Running the Local Server
`cd IBM-Hack-2019/energy-auditor/`
`python manage.py runserver`


## Notes on pushing to IBM Cloud

### Login details
* IBM Cloud ID: `rohanchacko007@gmail.com`
* Password: `Greenticks4$`

### Prerequisites
* Install IBMCloud CLI `curl -sL https://ibm.biz/idt-installer | bash
`  

After making changes to the app, run the following commands to push to IBM Cloud
```bash
ibmcloud login
ibmcloud target --cf
ibmcloud cf push Energy\ Auditor -b https://github.com/cloudfoundry/python-buildpack#v1.6.34
```

Navigate to `https://cloud.ibm.com/resources` and click on `Cloud Foundry Apps` and click on `Energy Auditor`

## Architecture

### Disaggregation model architecture
<p align="center">
  <img src="https://github.com/RohanChacko/IBM-Hack-2019/blob/master/assets/model.png" alt="Disaggregation Model  "/>
</p>

## Implementation details

* Python version - 3.6
* Framework - Django
* Frontend - Bootstrap
* ML Model trained on - Keras on Tensorflow
* Input from user - Provides monthly electricity bills as input to the app

## Directory Structure

```
.
├── assets
├── docs
│   ├── Ideation Document.pdf
│   └── Undertaking Form.pdf
├── energy-auditor
│   ├── db.sqlite3
│   ├── energyaudit
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── for_demo.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── management
│   │   ├── migrations
│   │   ├── model.png
│   │   ├── models.py
│   │   ├── predictapi2.py
│   │   ├── predictapi.py
│   │   ├── __pycache__
│   │   ├── shortseq2pointdisaggregator.py
│   │   ├── static
│   │   ├── templates
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── environment.yml
│   ├── greenticks
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── settings
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   ├── manifest.yml
│   ├── model.png
│   ├── Procfile
│   ├── requirements.txt
│   └── runtime.txt
├── model15min
└── README.md

```

* `assets/` contains images, diagrams, etc
* `docs/` contains the required documentation - Undertaking doc, Ideation doc, Presentation
* `energy-auditor/` directory contains the source code for the application
* `energy-auditor/greenticks/` directory contains the source code for the main application
* `energy-auditor/energyaudit/` directory contains static files, templates, models, forms, etc
