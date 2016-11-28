import sqlite3

DATABASE = 'blog.db'


def setup_db():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS posts( title TEXT, blog TEXT)")
    db.commit()
    cur.execute("SELECT COUNT(*) FROM posts")
    cur.execute('INSERT INTO posts(title, blog) VALUES("First entry", "Created by Vaida Abelkyte 20016 - for Data Representation and Querying ")')

    db.commit()
        
        
if __name__ == "__main__":

    setup_db()   
   