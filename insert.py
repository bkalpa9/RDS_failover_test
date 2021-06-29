from time import sleep
from database import *


pg = get_pg_write_conn()


def insert_data(pg):
    try:
        # print("insert data ......................................")

        sql = """
                INSERT INTO t_random VALUES (generate_series(1,2), md5(random()::text));
                """

        pg.execute(sql)
        # print("Successfully inserted data to postgres ..........................")
        return pg.statusmessage
    except Exception as e:
        print(
            "error innserting status data to postgres ..........................",
            str(e),
        )
if __name__ == "__main__":
    while True:
        print(insert_data(pg))
        sleep(1)