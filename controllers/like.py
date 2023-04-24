from flask_app import app
from flask import   redirect
from flask_app.models.like_model import Like


@app.route('/add_like/<int:tvshow_id>/<int:user_id>', methods=['POST'])
def add_like(tvshow_id, user_id):
    Like.add_like(tvshow_id, user_id)
    return redirect('/shows')

@app.route('/remove_like/<int:tvshow_id>/<int:user_id>', methods=['POST'])
def remove_like(tvshow_id, user_id):
    Like.remove_like(tvshow_id, user_id)
    return redirect('/tvshow')
