from flask import render_template,flash,request, current_app, redirect, url_for, session, after_this_request, send_file

from extensions import db

def configure_views(app):


	@app.route("/", methods=['GET'])
	def index():
		return render_template("index.html")

	

