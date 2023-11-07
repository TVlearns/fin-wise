# FinWise

FinWise is a comprehensive finance tracker that allows users to manage their financial life with ease. With secure user authentication, users can create, edit, view, and delete various financial elements such as budgets, savings, transactions, and bills. The application also supports bulk uploads of transactions through CSV files, making it easy to keep track of financial data.

## Features

User Authentication: Secure signup and login processes to protect user data.
Finance Management: Create, edit, view, and delete budgets, savings, and bills.
Transaction Handling: Log and categorize transactions with ease.
Bulk Uploads: Import transaction data in bulk via CSV format.
Interactive Dashboard: Visualize financial data with a beautiful chart.

## Technologies Used

Frontend: Vite, React, JavaScript, HTML, CSS
Backend: Python, Django
Charts: Chartist, ECharts, Recharts
Date Handling: date-fns
Form Handling: react-papaparse
Styling: MUI
Dependencies
Below are the primary libraries and dependencies used in FinWise:

## Frontend

@mui/icons-material
@mui/x-date-pickers
axios
chartist
date-fns
echarts
react-papaparse
react-router-dom
recharts
tinycolor2

## Backend

Django REST Framework with Cookie and Token Authentication
Pagination support with REST Framework
Additional Django packages such as colorfield and corsheaders

## Setup

To set up the project locally, follow these steps:

```bash
# Clone the repository
git clone https://fin-wise.git
cd yourproject/frontend
# Install dependencies
npm install
# Start the frontend server
npm start
```

```bash
# Move to the backend directory
cd ../backend
# Setup a virtual environment (optional)
python -m venv venv
source venv/bin/activate # For Unix systems
# Install dependencies
pip install -r requirements.txt
# Start the backend server
python manage.py runserver
```

## Usage

After setting up the project, you can access the FinWise application in your browser at http://localhost:3000.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.


