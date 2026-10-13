# 📚 Reading Dashboard

A wide-layout Streamlit dashboard that tracks books read, ratings, and reading goals, with sidebar filters, metrics, and tabs.

## Features

- **Sidebar filters**
  - **Genre** (selectbox): filters the metrics, chart, and book list
  - **Yearly reading goal** (slider): updates the progress bar and sidebar progress metric
  - **Include 'To Read' books** (checkbox): shows or hides books not started yet
- **Metrics row**: Books Finished, Pages Read, and Avg Rating, each with a delta value
- **Overview tab**: bar chart of pages read by genre and a yearly goal progress bar
- **Details tab**: full table of books with title, author, genre, pages, rating, and status
- **About expander**: explains how the dashboard works

## Tech Stack

- Python
- Streamlit
- pandas

## Getting Started

1. Clone the repo and move into the folder:

   ```bash
   git clone https://github.com/Lena6779/Reading-Dashboard.git
   cd Reading-Dashboard
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install streamlit pandas
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

   The dashboard opens in your browser at `http://localhost:8501`.

## Data

All book data is hardcoded in `app.py` as a pandas DataFrame. The focus of this project is on Streamlit layout rather than data fetching. Ratings are only given to finished books, and the Avg Rating delta compares against last year's average of 3.8.

## Requirements Covered

| Requirement | Implementation |
|---|---|
| Page config | `st.set_page_config()` with `layout="wide"`, title, and 📚 icon |
| Sidebar controls | Selectbox, slider, and checkbox that filter the main content |
| Metrics row | 3 `st.metric()` cards in `st.columns(3)` with deltas |
| Tabs | "Overview" and "Details" tabs with different content |
| Expander | "About this dashboard" with supplementary info |
| Hardcoded data | 10 YA and fiction books in a pandas DataFrame |