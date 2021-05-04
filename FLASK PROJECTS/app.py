from flask import Flask, render_template, url_for, request, redirect, session, send_file
from markupsafe import escape
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import Form, StringField, SubmitField, RadioField, DateTimeField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_mysqldb import MySQL
from MySQLdb.cursors import DictCursor
#import mysql.connector

app = Flask(__name__)
app.config["SECRET_KEY"] = 'mysecretkey'

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'ecom_app'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# mydb = mysql.connection.cursor(
#    host="127.0.0.1", user="root", password="root", database="ecom_app")
#mycursor = mydb.cursor(dictionary=true)

mysql = MySQL(app)

limit = 2


@app.route('/', methods=['GET', 'POST'])
def root():
    cur = mysql.connection.cursor(cursorclass=DictCursor)

    cur.execute('''select * from products''')
    count = cur.rowcount
    pages = round(count/limit)

    if request.method == "POST":

        req = request.form

        search = req.get("search")

        sql = 'select * from products WHERE product_name LIKE %s'
        args = [search+'%']
        cur.execute(sql, args)
        results = cur.fetchall()
        count_search = cur.rowcount
        pages_search = round(count_search/limit)

        if request.args.get("page") is None:
            search_page_no = 1

        else:
            search_page_no = int(request.args.get("page"))

        search_offset_val = (search_page_no - 1) * limit

        sql_search = "select * from products WHERE product_name LIKE %s ORDER BY product_id DESC LIMIT %s OFFSET %s"
        args_search = [search+'%', limit, search_offset_val]
        #args_s = [search+'%'], limit, search_offset_val
        cur.execute(sql_search, args_search)
        results_search = cur.fetchall()

        return render_template('index.html', p_count=pages_search, data=results_search)

    else:

        if request.args.get("page") is None:
            page_no = 1

        else:
            page_no = int(request.args.get("page"))

        offset_val = (page_no - 1) * limit

        cur.execute(
            '''select * from products ORDER BY product_id DESC LIMIT %s OFFSET %s''', (limit, offset_val))
        results = cur.fetchall()

    # message = 'Flask server is running.'
    return render_template('index.html', p_count=pages, data=results)


@app.route('/admin')
def admin():
    return render_template('admin/Login/Login.html')


@app.route('/login')
def login():
    return render_template('admin/Login/Login.html')


@app.route('/signup')
def signup():
    return render_template('admin/Login/signup.html')


@app.route('/products', methods=['GET', 'POST'])
def product():

    cur = mysql.connection.cursor(cursorclass=DictCursor)
    cur.execute('''select * from products''')
    results = cur.fetchall()

    return render_template('admin/products/products.html', data=results)


@app.route('/products/create', methods=['POST'])
def create_product():
    if request.method == 'POST':
        name = escape(request.form['item_name'])
        pro_type = int(escape(request.form['pro_type']))
        price = float(escape(request.form['price']))
        description = escape(request.form['pro_description'])
        img_path = escape(request.form['img_path'])
        print(type(name), type(pro_type), type(price),
              type(description), type(img_path))
        try:
            cur = mysql.connection.cursor()
            sql = """INSERT INTO item_details (product_name, product_type_id, price, product_description, img_path) VALUES (%s, %s, %s, %s, %s)"""
            val = (name, pro_type, price, description, img_path)
            cur.execute(sql, val)
            mysql.connection.commit()
            if cur.rowcount > 0:
                print("insertion Successfull")

        except Exception as e:
            print(e)
        return redirect(url_for('product'))

    return render_template('admin/products/products.html')


if __name__ == "__main__":
    app.run(debug=True)
