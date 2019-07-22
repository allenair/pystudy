#-*- coding: utf-8 -*-

import psycopg2

def insert_update(sqlst=[],
                  database="ask_order_db",
                  user="aistudy",
                  password="aistudy@zxtech",
                  host="192.168.1.147",
                  port="5432"):
    conn = psycopg2.connect(database=database,
                            user=user,
                            password=password,
                            host=host,
                            port=port)
    if not sqlst:
        return ''

    cur = conn.cursor()
    for sql in sqlst:
        cur.execute(sql)
    conn.commit()
    conn.close()
    return 'OK'


def search(sql='',
           database="ask_order_db",
           user="aistudy",
           password="aistudy@zxtech",
           host="192.168.1.147",
           port="5432"):
    conn = psycopg2.connect(database=database,
                            user=user,
                            password=password,
                            host=host,
                            port=port)

    if not sql:
        return []

    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()

    return rows


# rows = search(sql='select * from std_word limit 20')
# for row in rows:
#     print(row)

# with open('d:/res.txt','w') as fout:
#     for row in rows:
#         for item in row:
#             fout.write(str(item)+"  ")
#         fout.write('\n')
