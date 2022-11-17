## MESARATI PROJECT

- Data was extracted from wikepedia (link) using google sheets and then downloaded intto the root
    of the project learnt from this (tutorial)[https://www.youtube.com/watch?v=RJXPlVCcYRE]

- Data is cleaned to remove metrics from values, (using split to columns from the Data tab on Google sheets) displacement is in cubic metres and power is in brake horse power (bhp), then format them as numbers.

- Use pip to instal openpyxl

- Copy the dependencies in the tensorflow-test environment yml file and paste them in this environment

- syntax for quarantining any application "$ xattr -d com.apple.quarantine chromedriver "

- Grafana is is installed for visualisation. using "brew install grafana" and started up with "brew services start grafana"
-  The default HTTP port that Grafana listens to is 3000 unless you have configured a different port. admin as username.
- Install google sheets plugin on Grafana on the web
- enable Google Sheets API via this https://console.cloud.google.com/apis/library/sheets.googleapis.com?q=sheet and
    the Google drive API via https://console.cloud.google.com/apis/library/drive.googleapis.com?q=drive

- pip install slqalchemy, sqlalchemy, it is a client for managing databases; writing sql code in python
## Setting up PostgresSQL,
- Go pgadmin4,select object, then register, server
- the name PostgreSQL 14 is put as name and localhost is put has Hostname/address on the connection tab