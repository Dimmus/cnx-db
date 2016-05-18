# -*- coding: utf-8 -*-
import psycopg2


def test_db_init(connection_string, db_wipe):
    from cnxdb.init.main import init_db
    init_db(connection_string)

    def table_name_filter(table_name):
        return (not table_name.startswith('pg_') and
                not table_name.startswith('_pg_'))

    with psycopg2.connect(connection_string) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT table_name "
                           "FROM information_schema.tables "
                           "ORDER BY table_name")
            tables = [table_name for (table_name,) in cursor.fetchall()
                      if table_name_filter(table_name)]

    assert 'modules' in tables
    assert 'pending_documents' in tables
