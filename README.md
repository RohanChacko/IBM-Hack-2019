# IBM-Hack-2019
## Topic: Energy Audit for households

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

* Suggestions (can be combined with dashboard)
  * Display suggestions/tips/recommendations to help user save energy

* Leaderboard
  * Display user's position w.r.t to other people in locality and friends

* Account
  * Change password/edit basic user details, location, etc
  * Ability to add/remove appliances from existing list

## TODO

| Checkbox  | Task       | Assigned   |
| :---------| :--------- | :--------- |
| &#9744;   | Set up basic infrastructure | Aadil |
| &#9744;   | Set up user authentication (OAuth or custom) | Anyone |
| &#9744;   | Integrate Watson APIs into the app | Anyone |
| &#9744;   | Choose a database location for storage (cloud/storage) | Anyone |
| &#9744;   | Get user's friends (and/or) aggregate people based on location vicinity for leaderboard. If going with friends, need to find a way to get user's friends info. If going with people in vicinity, need to get vicinity information | Anyone |
| &#9744;   | Documentation (README, ppt, code comments, video) | EVERYONE |
