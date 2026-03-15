from db import get_db
def add_long_url(codes,long_url):
    conn=None
    try:
        conn = get_db()
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO urls (code, long_url) VALUES (%s, %s)",
                (codes, long_url)
            )

            conn.commit()
    finally:
        if conn:
            conn.close()
    return {"msg":"successfully inserted"}

def get_url(codes):
    conn=None
    try:
        conn = get_db()
        with conn.cursor() as cursor:
            cursor.execute("SELECT  long_url FROM urls WHERE code = %s", (codes,))
            result = cursor.fetchone()
            if result:
                return result[0]


            return None


    finally:
        if conn:
            conn.close()


