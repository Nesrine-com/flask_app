from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.tvshows_model import Tvshow
from flask_app.models.like_model import Like


@app.route('/shows/new')
def New_show():
    if 'user_id' not in session:
          return redirect('/')
    return render_template('new_tvshow.html')


@app.route('/tvshows/create', methods=['post'])
def create_tvshow():
     
     if not Tvshow.validate(request.form):
          return redirect('/shows/new')
     
     data={
          **request.form,
          'user_id':session['user_id']
     }
     Tvshow.create_tvshow(data)
     return redirect('/shows')
@app.route('/shows/edit/<int:tvshow_id>')
def edit(tvshow_id):
     if 'user_id' not in session:
          return redirect('/')
     tvshow=Tvshow.get_by_id({'id':tvshow_id})
     return render_template('edit.html',tvshow=tvshow)
@app.route('/tvshows/Edit', methods=['post'])
def update():
     if not Tvshow.validate(request.form):
          return redirect('/shows/edit/'+ request.form['id'])
     Tvshow.update(request.form)
     return redirect('/shows')

@app.route('/shows/delete/<int:tvshow_id>')
def destroy(tvshow_id):
     Tvshow.delete({'id':tvshow_id})
     return redirect('/shows')

@app.route('/shows/<int:tvshow_id>')
def view(tvshow_id):
     tvshow=Tvshow.get_by_id({'id':tvshow_id})
     return render_template('view.html', tvshow=tvshow)


     
