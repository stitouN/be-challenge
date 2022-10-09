from models.beDb  import Users, db


def get_users_by_page(page,max_items):
    data = Users.query.order_by(Users.user_id.desc()).paginate(page=page,per_page=max_items)
    return data



def searchUsersByFirstName(firstname):
    data = Users.query.filter_by(firstname=firstname).all()
    return data


def commit_changes():
    db.session.commit()