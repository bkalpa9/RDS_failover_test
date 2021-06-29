# RDS Failover Test

1. clone the github repo
2. connect to your development postgres server and create table using test_table.sql
3. cd to RDS_failover_test directory

4. get the endpoint of develop postgres server and add them into .env file
```
    postgres://<username>:password@<db endpoint>:port/<database where table was created>
```
4. create virtual environment 
   ```
    python3 -m venv rds
    source rds/bin/activate

   ```
5. install all requirements by running:
```
    pip install -r requirements.txt

```
6. run select.py file to check if database connection is working

```
    python select.py

```
