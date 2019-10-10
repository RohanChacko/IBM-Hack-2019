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
conda env create -f environment.yml
conda activate ibmhack
pip install -r requirements.txt
```

## Run app locally

* Running the Local Server
```
cd IBM-Hack-2019/energy-auditor/
python manage.py runserver
```

## Implementation details

* Python version - 3.6
* Framework - Django
* Frontend - Bootstrap
* ML Model trained on - Keras on Tensorflow
* Input from user - Provides monthly electricity bills as input to the app

## Architecture

### Disaggregation model architecture
<p align="center">
  <img src="https://github.com/RohanChacko/IBM-Hack-2019/blob/master/assets/model.png" alt="Disaggregation Model"/>
</p>

### Architecture Flow Diagram
<p align="center">
  <img src="https://github.com/RohanChacko/IBM-Hack-2019/blob/master/assets/crp_arch_flow.png" alt="Architecture Flow"/>
</p>

## Directory Structure

```
.
├── assets
├── docs
│   ├── Ideation Document.pdf
│   ├── Presentation.pptx
│   └── Undertaking Form.pdf
├── energy-auditor
│   ├── db.sqlite3
│   ├── energyaudit
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── experiment.py
│   │   ├── for_demo.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── management
│   │   ├── migrations
│   │   ├── model.png
│   │   ├── models.py
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
├── ML snippets
│   ├── iawe-test2.py
│   ├── iawetrain.py
│   ├── metrics.py
│   ├── Results.txt
│   └── shortseq2pointdisaggregator.py
├── model15min
├── README.md
└── venv


```

* `assets/` contains images, diagrams, etc
* `docs/` contains the required documentation - Undertaking doc, Ideation doc, Presentation
* `energy-auditor/` directory contains the source code for the application
* `energy-auditor/greenticks/` directory contains the source code for the main application
* `energy-auditor/energyaudit/` directory contains static files, templates, models, forms, etc

## Notes

* Registered accounts
  * ID: chacko | Password: greenticks
  * ID: greenticks | Password: blueticks
* Since disaggregation takes time, we have put a stub for demonstration purposes. Viewing it locally with the set values will be easier to understand the proof-of-concept. The set values can be easily replaced with appropriate variables when required in production. With more computational power, the disaggregation can be made done faster.
