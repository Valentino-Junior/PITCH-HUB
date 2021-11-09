from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User, Comment, Upvote, Downvote
from .forms import PitchForm, CommentForm, UpvoteForm, UpdateProfile
from flask.views import View, MethodView
from .. import db, photos
import markdown2


# Views
@main.route('/', methods=['GET', 'POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitch = Pitch.query.filter_by().first()
    title = 'Home'
    businesspitch= Pitch.query.filter_by(category="businesspitch")
    interviewpitch = Pitch.query.filter_by(category="interviewpitch")
    techpitch = Pitch.query.filter_by(category="techpitch")
    pickuppitch = Pitch.query.filter_by(category="pickuppitch")

    upvotes = Upvote.get_all_upvotes(pitch_id=Pitch.id)

    return render_template('index.html', title=title, pitch=pitch, pickuppitch=pickuppitch,
                           interviewpitch=interviewpitch, businesspitch=businesspitch, techpitch=techpitch,
                           upvotes=upvotes)



@main.route('/pickup', methods=['GET', 'POST'])
def pickup():
    pitch = Pitch.query.filter_by().first()
    pickuppitch = Pitch.query.filter_by(category="pickuppitch")
    return render_template('pick-up.html', pitch=pitch, pickuppitch=pickuppitch)

@main.route('/business', methods=['GET', 'POST'])
def business():
    pitch = Pitch.query.filter_by().first()
    businesspitch= Pitch.query.filter_by(category="businesspitch")

    return render_template('business.html', businesspitch=businesspitch, pitch=pitch)

@main.route('/interview', methods=['GET', 'POST'])
def interview():
    pitch = Pitch.query.filter_by().first()
    interviewpitch = Pitch.query.filter_by(category="interviewpitch")

    return render_template('interview.html', pitch=pitch, interviewpitch=interviewpitch)

@main.route('/technology', methods=['GET', 'POST'])
def technology():
    techpitch = Pitch.query.filter_by(category="techpitch")
    pitch = Pitch.query.filter_by().first()
    return render_template('technology.html', pitch=pitch, techpitch=techpitch)

@main.route('/pitches/new/', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    my_upvotes = Upvote.query.filter_by(pitch_id=Pitch.id)
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id=current_user._get_current_object().id, title=title, description=description,
                          category=category)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('pitches.html', form=form)


@main.route('/comment/new/<int:pitch_id>', methods=['GET', 'POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description=description, user_id=current_user._get_current_object().id, pitch_id=pitch_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', pitch_id=pitch_id))

    all_comments = Comment.query.filter_by(pitch_id=pitch_id).all()
    return render_template('comments.html', form=form, comment=all_comments, pitch=pitch)


@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods=['GET', 'POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id=pitch_id)

    if Upvote.query.filter(Upvote.user_id == user.id, Upvote.pitch_id == pitch_id).first():
        return redirect(url_for('main.index'))

    new_upvote = Upvote(pitch_id=pitch_id, user=current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))


@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods=['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id=pitch_id)

    if Downvote.query.filter(Downvote.user_id == user.id, Downvote.pitch_id == pitch_id).first():
        return redirect(url_for('main.index'))

    new_downvote = Downvote(pitch_id=pitch_id, user=current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index'))



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()