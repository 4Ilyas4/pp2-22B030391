import psycopg2


connection = psycopg2.connect(    
    database="firstdb",
    user="postgres",
    password="4PraeToriaN4",
    host="localhost",
    port="5432")
cur = connection.cursor()

cur.execute("""
    CREATE OR REPLACE FUNCTION insert_user(vname text, vphone text) RETURNS void AS $$
    BEGIN
        IF EXISTS (SELECT * FROM  profil WHERE name = vname) THEN
            UPDATE profil SET phone = vphone WHERE name = vname;
        ELSE
            INSERT INTO  profil (name, phone) VALUES (vname, vphone);
        END IF;
    END;
    $$ LANGUAGE plpgsql;
""")
cur.execute("""
    CREATE OR REPLACE FUNCTION delete_user(vname text, vphone text) RETURNS void AS $$
    BEGIN
        IF vname IS NOT NULL THEN
            DELETE FROM profil WHERE name = vname;
        ELSIF vphone IS NOT NULL THEN
            DELETE FROM profil WHERE phone = vphone;
        END IF;
    END;
    $$ LANGUAGE plpgsql;
""")
cur.execute("""
CREATE OR REPLACE FUNCTION get_users(limits int, offsets int) RETURNS TABLE (vid int,vname text, vphone text) AS $$
BEGIN
    RETURN QUERY SELECT id, name, phone FROM profil LIMIT limits OFFSET offsets;
END;
$$ LANGUAGE plpgsql;""")
connection.commit()
cur.close()
connection.close()
    
