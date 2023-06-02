import mariadb
import dbcreds

# conn = mariadb.connect(**dbcreds.conn_params)
# cursor = conn.cursor()
# cursor.execute('CALL get_all_items()')
# results = cursor.fetchall()
# cursor.close()
# conn.close()

# for i in range(len(results)):
#     print(results[i][1])
#     print(results[i][2])

def filter_items():
    try:
        print("Return all items priced over X, where X is? ")
        user_input = int(input())
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute('CALL get_items_over_input(?)', [user_input])
        items = cursor.fetchall()
        cursor.close()
        conn.close()        
        for y in range(len(items)):
            print(str(items[y][1], 'utf-8'))
            print(items[y][2])
    except:
        print("Something went wrong")

filter_items();