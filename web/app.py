from flask import Flask, jsonify, request, render_template,send_from_directory,send_file
from addressparser.addressparser import AddressParser
import os

parser = AddressParser()
app = Flask(__name__)

app.config['Data_Uploads'] = '/Users/adarshghimire/Desktop/web/static/uploads'

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/datauploads", methods=['GET', 'POST'])
def datauploads(): 
    if request.method == 'POST' and 'csv_data' in request.files:
        file = request.files['csv_data']
        filename = file.filename
        file.save(os.path.join(app.config['Data_Uploads'], filename))

        file_path = get_file_path(filename)

        df = parser.parse_csv(file_path, cols=[6])
        print(get_file_path(filename+'_parsed.csv'))
        df.to_csv(get_file_path('new_parsed.csv'),index=False)

    return render_template('details.html', filenames = file_path)

@app.route("/download", methods=['GET'])
def download(filename='new_parsed.csv'):
    if request.method == 'GET':
        uploads = app.config['Data_Uploads']
        path = uploads+'/'+filename
        return send_file(path,mimetype='text/csv',attachment_filename=filename,as_attachment=True)

def get_file_path(filename):
    return os.path.join(app.config['Data_Uploads'], filename)
# @app.route("/predict", methods=['GET', 'POST'])
# def predict():
#     file_path = os.path.join('/Users/adarshghimire/Desktop/web/static/uploads/parsed.csv')
#     df = parser.parse_csv(file_path, cols=[6])
#     print(df)

    # return render_template('predict.html')


if __name__ == "__main__":
    app.run(debug=True)