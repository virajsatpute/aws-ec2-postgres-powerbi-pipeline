# Cloud Analytics Pipeline with Power BI

An end-to-end data pipeline that loads sales data into PostgreSQL on an AWS EC2 server using Python, refreshes it on a schedule with cron, and serves a Power BI dashboard.

<img width="1344" height="755" alt="Image" src="https://github.com/user-attachments/assets/e5c0e7c9-35fc-4c84-b478-26622bb9ab65" />

## Architecture

<img width="975" height="456" alt="Image" src="https://github.com/user-attachments/assets/ff29e1e4-6193-4a1b-a0ed-37b87a13d5f6" />

Dataset CSV -> EC2 (Ubuntu) -> Python ETL (pandas, SQLAlchemy) -> PostgreSQL -> Power BI (via SSH tunnel)

## Tools

AWS EC2, Ubuntu, PostgreSQL, Python (pandas, SQLAlchemy, psycopg2), cron, SSH tunneling, Power BI, DAX

## What the pipeline does

- Extracts the Superstore sales dataset from a CSV file
- Cleans column names, removes duplicates, and parses day-first dates
- Loads the cleaned data into a PostgreSQL database on an EC2 instance
- Reruns daily through a cron job
- Connects Power BI to PostgreSQL through a secure SSH tunnel, so the database port is never exposed to the internet

## Dashboard

KPI cards for total sales, orders, customers, and average delivery days, plus breakdowns by region, category, sub-category, ship mode, and month, with slicers for region and segment.

## Key insights

- West is the top region by sales, and South is the lowest
- Technology is the top category
- Phones and Chairs lead the sub-categories
- Standard Class accounts for about 59% of sales, and average delivery takes about 4 days
- Sales peak every November-December, and the peaks grow each year

## Proof of deployment

<img width="1694" height="235" alt="Image" src="https://github.com/user-attachments/assets/98339b4d-7bdc-46f2-95fb-4b7ac2eb78f4" />
<img width="1128" height="39" alt="Image" src="https://github.com/user-attachments/assets/370337cb-74f1-4f09-b701-9857c584bb1c" />

## How to run

1. Launch an Ubuntu EC2 instance and install PostgreSQL and Python
2. Create a `sales` database and an `etl` user
3. Upload the CSV and run `python etl.py` (set your own password in the script)
4. Schedule it with cron
5. Connect Power BI to `localhost:5433` through an SSH tunnel

Full commands are in [setup_commands.md](setup_commands.md).

## Notes

- The EC2 instance and all related AWS resources were terminated after the project to avoid charges
- Credentials in the code are placeholders (`YOUR_PASSWORD`)

---
## 🌟 Author
**Viraj Satpute**  
Data Analyst | Power BI | Cloud Computing (AWS)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/virajsatpute/)
