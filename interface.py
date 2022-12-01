# Importing Required Libraries
from flask import Flask,render_template,request,jsonify
from Project_Data.utils import Heart_Disease

app = Flask(__name__)


# BASE API

@app.route('/')
def Hello():
    print('This is Base API')
    return render_template('index.html')

# Submit API
@app.route('/submit',methods = ['POST','GET'])
def submit():
    if request.method == 'POST':

        age =       float(request.form ['age'])
        sex =       str(request.form ['sex'])
        cp =        float(request.form ['cp'])
        trestbps =  float(request.form ['trestbps'])
        chol =      float(request.form ['chol'])
        bs =        float(request.form ['bs'])
        restecg =   float(request.form ['restecg'])
        thalach =   float(request.form ['thalach'])
        exang =     float(request.form ['exang'])
        oldpeak =   float(request.form ['oldpeak'])
        slope =     float(request.form ['slope'])
        ca =        float(request.form ['ca'])
        thal =      float(request.form ['thal'])

        Heart_Dis = Heart_Disease(age,sex,cp,trestbps,chol,bs,restecg,
                            thalach,exang,oldpeak,slope,ca,thal)
        hd = Heart_Dis.Get_Disease_Prediction()

        return render_template('result.html',result = hd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 1111)