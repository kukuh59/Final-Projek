from flask import Flask, render_template, url_for, redirect, request
from mysql import connector

app = Flask(__name__)

db = connector.connect(
    host    = "localhost",
    user    = "root",
    passwd  = "",
    database= "kost_baru"
)

if db.is_connected():
    print("===========Connected=========")


@app.route('/')
@app.route('/home')
def home():

    cur = db.cursor()
    cur.execute('select * from kamar;')
    hasil = cur.fetchall()
    cur.close()
    return render_template('home.html', title='IN DE KOST-Nyaman Dan Murah', hasil=hasil)


@app.route('/about')
def about():
    return render_template('about.html', title='About US')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')


@app.route('/booking/<kamar>', methods=['GET', 'POST'])
def booking(kamar):
    if request.method == 'POST':
        kamar = kamar
        no_ktp = request.form['no_ktp']
        nama = request.form['nama']
        no_hp = request.form['no_hp']
        kota_asal = request.form['kota_asal']

        cur = db.cursor()
        cur.execute('insert into penyewa (no_ktp, nama, no_hp, kota_asal) values (%s, %s, %s, %s)',
                    (no_ktp, nama, no_hp, kota_asal))
        db.commit()
        cur.close()

        return redirect(url_for('home'))
    return render_template('booking.html', title='Booking', kamar=kamar)


@app.route('/tes')
def tes():
    return render_template('about.html', title='About US')


if __name__ == "__main__":
    app.run(debug=True)




# @app.route('/proses_tambah/', methods=['POST'])
# def proses_tambah():
#     kode_penyewa = request.form['kode_penyewa']
#     nama_penyewa = request.form['nama_penyewa']
#     jenis_kelamin = request.form['jenis_kelamin']
#     no_hp = request.form['no_hp']
#     asal = request.form['asal']
#     cur = db.cursor()
#     cur.execute("INSERT INTO penyewa (kode_penyewa, nama_penyewa, jenis_kelamin, no_hp, asal) VALUES (%s, %s, %s, %s, %s)",
#                 (kode_penyewa, nama_penyewa, jenis_kelamin, no_hp, asal))
#     db.commit()
#     return redirect(url_for('halaman_utama'))

#
# @app.route('/ubah/<kode_penyewa>', methods=['GET'])
# def ubah_data(kode_penyewa):
#     cur = db.cursor()
#     cur.execute("select * from penyewa where kode_penyewa=%s",(kode_penyewa,))
#     res = cur.fetchall()
#     cur.close()
#     return render_template('ubah.html', hasil=res)
#
#
# @app.route('/proses_ubah/', methods=['POST'])
# def proses_ubah():
#     kode_penyewa = request.form['kode_penyewa']
#     nama_penyewa = request.form['nama_penyewa']
#     jenis_kelamin = request.form['jenis_kelamin']
#     no_hp = request.form['no_hp']
#     asal = request.form['asal']
#     cur = db.cursor()
#     sql = "update penyewa set kode_penyewa=%s, nama_penyewa=%s, jenis_kelamin=%s, no_hp=%s, asal=%s where kode_penyewa=%s"
#     val = (kode_penyewa, nama_penyewa, jenis_kelamin, no_hp, asal)
#     cur.execute(sql, val)
#     db.commit()
#     return redirect(url_for('halaman_utama'))
#
# @app.route('/hapus/<kode_penyewa>', methods=['GET'])
# def hapus_data(kode_penyewa):
#     cur= db.cursor()
#     cur.execute("DELETE from penyewa where kode_penyewa=%s", (kode_penyewa,))
#     db.commit()
#     return  redirect(url_for('halaman_utama'))





