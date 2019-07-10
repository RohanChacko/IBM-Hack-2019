# IBM-Hack-2019
## Topic: Energy Audit for households
#### Team: Greenticks

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

The app is live on: `https://energy-auditor.eu-gb.mybluemix.net`

## Modules

* Welcome/Home
  * With app name/logo and random facts about saving energy, etc with route to Login/Register

* Login/Register
  * For register - Basic user auth using OAuth or otherwise. Routes user to User Details
  * For login - Basic login page. Takes user to Dashboard

* User Details (First time users only).
  * Ask a survey of questions including but not limited to
    * List of appliances
    * Past monthly bills(?) (optional)
    * Family size
    * Features of the homes (no. of rooms, house facing direction, location, etc)

  Directs user to Dashboard.

* Dashboard
  * Contains graphs, statistics, basic data visualizations.
  * Prominently shows user how much energy/money user has saved after using the app

* Suggestions (can be combined with Dashboard)
  * Display suggestions/tips/recommendations to help user save energy

* Leaderboard
  * Display user's position w.r.t to other people in locality and friends

* Account
  * Change password/edit basic user details, location, etc
  * Ability to add/remove appliances from existing list

## TODO

| Checkbox  | Task                                                  | Assigned |
| :-------: | :---------                                            | :------: |
| &#9744;   | Set up basic infrastructure                           | Aadil    |
| &#9744;   | Scrap data for training model                         | Zubair, Athreya, Chacko |
| &#9744;   | Train the model and deploy                            | Zubair, Athreya, Chacko |
| &#9744;   | Integrate NILMTK into the app                         | Athreya  |
| &#9744;   | Set up user authentication (OAuth or custom)          | Anyone   |
| &#9744;   | Integrate Watson APIs into the app                    | Anyone   |
| &#9744;   | Choose database location for storage (cloud/storage)  | Anyone   |
| &#9744;   | Get user's friends (and/or) aggregate people based on location vicinity for leaderboard. If going with friends, need to find a way to get user's friends info. If going with people in vicinity, need to get vicinity information                                                         | Anyone   |
| &#9744;   | Documentation (README, ppt, code comments, video)     | EVERYONE |

## Other details

* Python version - 3.6
* Framework - Django
* Frontend  - Bootstrap
* Data assumption - User provides monthly electricity bills as input to the app

## Directory Structure

```
.
└── IBM-Hack-2019
    ├── README.md
    └── src
        ├── db.sqlite3
        ├── greenticks
        │   ├── __init__.py
        │   ├── settings
        │   │   ├── __init__.py
        │   │   ├── base.py
        │   │   ├── local.py
        │   │   └── production.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── manage.py
        └── requirements.txt
```


* `IBM-Hack-2019/src/` directory contains the source code for the application.
* `IBM-Hack-2019/src/greenticks` directory contains the source code for the main application.
* `IBM-Hack-2019/src/greenticks/settings/base.py` contains the base settings for the application.
* `IBM-Hack-2019/src/greenticks/settings/local.py` contains the local settings for the application, these settings are meant for local testing environments.
* `IBM-Hack-2019/src/greenticks/settings/production.py` contains the production settings for the application, these settings are meant for deployment purposes.

## Some Important Commands

* Running Migration
`cd IBM-Hack-2019/src/`
`python manage.py migrate`

* Creating Super Users
`cd IBM-Hack-2019/src/`
`python manage.py createsuperuser`

* Running the Local Server
`cd IBM-Hack-2019/src/`
`python manage.py runserver`


## Set up
```bash
virtualenv --python=python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Notes
* Do not push the venv directory. Maintain a local copy of it and install dependencies from `requirements.txt` as and when required
* Save all app related files outside venv
* `pip freeze > requirements.txt` everytime you install a new package
