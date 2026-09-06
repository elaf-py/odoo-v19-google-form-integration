# Odoo 19 - Google Form Integration

This module connects Google Forms with Odoo 19.

The idea came from a simple use case: keep Google Forms as an easy interface for users, but store and manage the submitted data inside Odoo instead of depending on Google Sheets.

### How it works

Google Form → Google Apps Script → API → Odoo

When a form is submitted, Apps Script sends the data to Odoo through a JSON-RPC endpoint.

Uploaded files are also retrieved from Google Drive and stored directly in Odoo as attachments.

### What is included

- Google Form submissions sent directly to Odoo
- File and PDF attachments
- API key authentication
- Unique submission ID to avoid duplicate records
- Approval stages inside Odoo
- Access groups for approvals

### Screenshots

#### Google Form
<img width="533" height="890" alt="image" src="https://github.com/user-attachments/assets/0837d770-9526-4a62-a433-b917d57907ee" />
https://docs.google.com/forms/d/e/1FAIpQLSdbzewaNpm3MO8WtoItEzfPDYA_JKnCyAdKfjCpRG3mfoQcMg/viewform?usp=dialog

#### Odoo Record
<img width="170" height="132" alt="image" src="https://github.com/user-attachments/assets/5bdaa9ac-7574-48e9-8fd2-8ed4947edfc0" />
<img width="1920" height="343" alt="image" src="https://github.com/user-attachments/assets/d12c7071-9568-4307-b386-3e6d9affb2f7" />

### Demo

https://lnkd.in/p/dgFMMyPa

### Tech

Odoo 19 / Python / XML / Google Apps Script / JSON-RPC / Google Drive

### Note

API keys and other credentials are not stored in the repository. They are configured using Odoo System Parameters and Google Apps Script Properties.

### Author

Elaf Amer
