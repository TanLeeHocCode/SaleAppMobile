from AppSale import app
from flask import Flask, render_template,request
import dao


@app.route("/")
def home():
    kw=request.args.get('kw')


    cast = dao.read_catesgory()
    pro = dao.read_products(kw)
    return render_template('index.html', cast=cast, pro=pro)


if __name__ == '__main__':
    app.run(debug=True)
