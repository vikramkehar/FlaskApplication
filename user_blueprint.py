# user_blueprint.py
from flask import Blueprint, request, jsonify
from models import db, User, Project

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/add-user', methods=['POST'])
def create_user():
    data = request.json
    print(data)
    username = data.get('username')
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    date_of_birth = data.get('date_of_birth')
    projectid = data.get( 'project_name' )

    if not username or not email:
        return jsonify({'error': 'Missing required fields'}), 400

    user = User(username=username, email=email, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth,projectid=projectid)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@user_blueprint.route('/userlist', methods=['GET'])
def get_all_users():
    users = User.query.all()
    projects = Project.query.all()
    project_data = {}
    for project in projects:
        project_data[project.project_id] = project.project_name
    result = []
    for user in users:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'date_of_birth': user.date_of_birth.strftime('%Y-%m-%d') if user.date_of_birth else None,
            'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            'project_name': project_data[user.projectid] if user.projectid else ""
        }
        result.append(user_data)
    return jsonify(result)

@user_blueprint.route('/getuser/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user_data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'date_of_birth': user.date_of_birth.strftime('%Y-%m-%d') if user.date_of_birth else None,
        'created_at': user.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        'project_name': [project.project_name for project in user.projects]
    }
    return jsonify(user_data)

@user_blueprint.route('/updateuser/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.json
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.date_of_birth = data.get('date_of_birth', user.date_of_birth)

    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@user_blueprint.route('/deleteuser/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    for project in user.projects:
        db.session.delete(project)


    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})




@user_blueprint.route('/add-project', methods=['POST'])
def create_project():
    data = request.json
    username = data.get('username')
    alloted_date = data.get('alloted_date')

    if not username or not alloted_date:
        return jsonify({'error': 'Missing required fields'}), 400

    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404


@user_blueprint.route('/projectlist', methods=['GET'])
def get_all_projects():
    projects = Project.query.all()
    result = []
    for project in projects:
        project_data = {
            'project_id': project.project_id,
            'project_name' : project.project_name,
            'alloted_date': project.alloted_date.strftime('%Y-%m-%d') if project.alloted_date else None,
            'username': project.username
        }
        result.append(project_data)
    return jsonify(result)
