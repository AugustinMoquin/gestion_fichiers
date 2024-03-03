import sqlite3

def get_table_size(conn, table_name):
    cursor = conn.cursor()

    query = """
        SELECT name AS table_name,
               (pgs.sz + coalesce(freepage, 0)) * pgs.pgsize AS table_size_bytes
          FROM (
              SELECT name,
                     file,
                     pgno,
                     pgsize,
                     max(pgcnt) AS freepage
                FROM (
                        SELECT name,
                              file,
                              pgno,
                              pgsize,
                              count(*) AS pgcnt
                         FROM (
                                SELECT name,
                                      file,
                                      pgno,
                                      pgsize
                                 FROM pragma_page_count,
                                      pragma_page_size
                                WHERE pragma_page_count.name = pragma_page_size.name
                                      AND pragma_page_count.name = ?
                               )
                         GROUP BY file,
                                  pgno
                   )
           LEFT JOIN pragma_freelist
           ON name = freelist
        GROUP BY name,
                 file,
                 pgno,
                 pgsize
      ) AS pgs;
    """

    cursor.execute(query, (table_name,))
    result = cursor.fetchone()

    cursor.close()

    if result:
        return result[1]  # Size in bytes
    else:
        return None
