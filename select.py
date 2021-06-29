from time import sleep
from database import *

pg = get_read_conn()


def get_data(pg):
    try:
        # print(pg)
        sql = """
                select count(*) from t_random ;
                """
        pg.execute(sql)
        query_result = pg.fetchall()

        # print("query Result....................\n", query_result)
        return query_result[0][0]
    except Exception as e:
        print(
            "error innserting status data to postgres ..........................",
            str(e),
        )


if __name__ == "__main__":
    while True:
        print("Total rows count : ",get_data(pg))
        sleep(1)