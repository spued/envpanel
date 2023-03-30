#!/usr/bin/env python3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('/home/sunya/envpanel/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ABCD1234567890ABCD'

@app.route('/')
def index():
    conn = get_db_connection()
    _data = conn.execute('SELECT * FROM env_data WHERE created > DATETIME("now", "localtime", "-24 hours")').fetchall()
    conn.close()
    return render_template('index.html', data=_data)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/messages')
def messages():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    motd_file = open("/home/sunya/envpanel/templates/motd.txt", "r")
    lines = motd_file.readlines()
    motd_file.close
    conn.close()
    return render_template('message.html', posts=posts, lines=lines)
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')
@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('messages'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

@app.route('/brightness', methods=('GET','POST'))
def brightness():
    if request.method == 'POST':
        #print(request.form)
        brightness_v = request.form['brightness_value']
        if not brightness_v:
            flash('Brightness is required!')
        else:
            print(brightness_v)
            conn = get_db_connection()
            conn.execute('UPDATE setting_data SET brightness = ?', (brightness_v,))
            conn.commit()
            conn.close()
    conn = get_db_connection()
    setting = conn.execute('SELECT * FROM setting_data').fetchone()
    conn.commit()
    conn.close()
    return render_template('brightness.html', setting = setting)
if __name__ == '__main__':
   app.run(host="0.0.0.0", debug = False)
