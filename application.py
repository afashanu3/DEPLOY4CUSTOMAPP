import sqlite3

DB_PATH = './todo.db'   # Update this path accordingly
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'

def add_to_list(book):
    try:
        conn = sqlite3.connect(DB_PATH)

        # Once a connection has been established, we use the cursor
        # object to execute queries
        c = conn.cursor()

        # Keep the initial status as Not Started
        c.execute('insert into items(book, finished) values(?,?)', (book, NOTSTARTED))

        # We commit to save the change
        conn.commit()
        return {"book": item, "finished": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None

def get_all_items():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_item(book):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select status from items where item='%s'" % book)
        status = c.fetchone()[0]
        return status
    except Exception as e:
        print('Error: ', e)
        return None
        
def update_status(book, finished):
    # Check if the passed status is a valid value
    if (finished.lower().strip() == 'not started'):
        finished = NOTSTARTED
    elif (finished.lower().strip() == 'in progress'):
        finished = INPROGRESS
    elif (finished.lower().strip() == 'completed'):
        finished = COMPLETED
    else:
        print("Invalid Status: " + finished)
        return None

    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update items set status=? where item=?', (finished, book))
        conn.commit()
        return {book: finished}
    except Exception as e:
        print('Error: ', e)
        return None

def delete_item(book):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from items where item=?', (book,))
        conn.commit()
        return {'book': book}
    except Exception as e:
        print('Error: ', e)
        return None
