# Enterprise Data Strategy Dashboard

An interactive Streamlit dashboard for analyzing first-year student dropout prediction and educational data strategy implementation.

## Overview

The dashboard provides institutional insights across seven key analytical pages:
- **Executive Overview** — Strategic KPIs and dropout rate reduction roadmap
- **Student Risk Intelligence** — Predictive model architecture and early-warning signals
- **Data Architecture** — Enterprise Lakehouse design specifications
- **Analytics Maturity** — Capability progression framework
- **Implementation Roadmap** — Three-phase deployment timeline
- **KPI Metrics** — Real-time performance tracking across four domains
- **ROI Analysis** — Interactive financial modeling and impact projections

## Features

- Professional white-themed UI with enterprise-grade design
- Interactive charts and visualizations (Plotly)
- Real-time KPI calculations
- Financial scenario modeling
- Responsive multi-page navigation
- Board-ready presentation format

## Installation

### Prerequisites
- Python 3.10+
- pip package manager

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/analytics-streamlit.git
cd analytics-streamlit
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the dashboard**
```bash
streamlit run dashboard.py
```

The dashboard will open at `http://localhost:8513`

## Deployment

### Option 1: Streamlit Cloud (Recommended)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Select your GitHub repository, branch, and `dashboard.py` file
5. Deploy!

### Option 2: Heroku

1. Create `Procfile`:
```
web: streamlit run dashboard.py --server.port=$PORT
```

2. Create `runtime.txt`:
```
python-3.12.0
```

3. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Option 3: AWS/Azure/GCP

Deploy as a containerized application using Docker:

```bash
docker build -t analytics-dashboard .
docker run -p 8513:8513 analytics-dashboard
```

## Project Structure

```
analytics-streamlit/
├── dashboard.py           # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # This file
└── Enterprise_Data_Strategy_Upgraded.docx  # Source document
```

## Technologies

- **Streamlit** — Web framework
- **Plotly** — Interactive visualizations
- **Pandas** — Data manipulation
- **NumPy** — Numerical computing

## Configuration

Create `.streamlit/config.toml` for custom settings:

```toml
[theme]
primaryColor = "#1e5a9e"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8fafb"
textColor = "#0d0d0d"

[server]
headless = true
port = 8513
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/feature-name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/feature-name`)
5. Open a Pull Request

## License

This project is confidential and for authorized users only.

## Support

For issues or questions, please contact the analytics team.

---

**Last Updated:** April 2026
**Status:** Production Ready
