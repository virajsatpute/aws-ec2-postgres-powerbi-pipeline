# Setup commands

## Connect to the server
```bash
ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>
```

## Install software (on the server)
```bash
sudo apt update
sudo apt install -y postgresql python3-pip python3-venv
python3 -m venv ~/etl-env
source ~/etl-env/bin/activate
pip install pandas sqlalchemy psycopg2-binary
```

## Create the database
```bash
sudo -u postgres psql
```
```sql
CREATE DATABASE sales;
CREATE USER etl WITH PASSWORD 'YOUR_PASSWORD';
\c sales
GRANT ALL ON SCHEMA public TO etl;
\q
```

## Upload data (from your laptop)
```bash
scp -i your-key.pem superstore.csv ubuntu@<EC2_PUBLIC_IP>:~/
```

## Run the pipeline (on the server)
```bash
python ~/etl.py
```

## Schedule daily at 2:00 UTC
```
0 2 * * * /home/ubuntu/etl-env/bin/python /home/ubuntu/etl.py >> /home/ubuntu/etl.log 2>&1
```

## Power BI connection (SSH tunnel, from your laptop)
```bash
ssh -i your-key.pem -L 5433:localhost:5432 ubuntu@<EC2_PUBLIC_IP>
```
Then in Power BI: PostgreSQL database, server `localhost:5433`, database `sales`.