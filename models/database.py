from models.beDb  import Users, db


def get_users_by_page(page,max_items):
    data = Users.query.order_by(Users.user_id.desc()).paginate(page=page,per_page=max_items)
    return data


def searchUsersByName(firstname,lastname):
    data = Users.query.filter_by(firstname=firstname,lastname=lastname).all()
    return data

def commit_changes():
    db.session.commit()