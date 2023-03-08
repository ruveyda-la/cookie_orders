from flask_app.models.order import Order
from flask_app import app
from flask import render_template, request, redirect,session,flash

@app.route("/cookies")
def read_all():
    orders = Order.get_all()
    return render_template("read.html", orders=orders)

@app.route("/cookies/new")
def show_form():
    return render_template("create.html")

@app.route("/cookies/new/create",methods=['POST'])
def create():
    if not Order.validate_order(request.form):
        session['name']= request.form['name']
        session['cookie_type']=request.form['cookie_type']
        session['number']=request.form['number']
        return redirect("/cookies/new")

    Order.save(request.form)
    print(request.form)
    return redirect("/cookies")

@app.route("/cookies/edit/update", methods=['POST'])
def update():
    id=request.form['id']
    print(request.form)
    if not Order.validate_order(request.form):
        return redirect(f"/cookies/edit/{id}")
    Order.change(request.form)
    return redirect ("/cookies")

@app.route("/cookies/edit/<int:id>")
def edit(id):
    data={'id':id}
    order= Order.get_one(data)
    return render_template('edit.html',order=order)
