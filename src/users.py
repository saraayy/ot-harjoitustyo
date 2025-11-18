import db

def get_user(user_id):
    sql = "SELECT id, username FROM users WHERE id = ? "
    return db.query(sql, [user_id])[0]


def get_tasks(user_id):
    sql = "SELECT id, task FROM tasks WHERE user_id = ? ORDER BY id DESC"
    return db.query(sql, [user_id])