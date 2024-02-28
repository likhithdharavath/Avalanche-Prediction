from flask import Flask,request,render_template,redirect,url_for
import pickle
app=Flask('__name__')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def load_form():
    return render_template('form.html')

@app.route('/prediction',methods=['POST'])
def predict():
    snow_pack_depth=float(request.form['data1'])
    snow_density=float(request.form['data2'])
    slope_angle=float(request.form['data3'])
    temperature_gradient=float(request.form['data4'])
    snow_intensity=float(request.form['data5'])
    # Load the trained model from model.pkl
    with open(r'C:\Users\dsai9\Projects\Avalanche Prediction\model\random_forest_classifier.pkl', 'rb') as f:
        model=pickle.load(f)
        
    #Let's predict
    input_data=[[snow_pack_depth,snow_density,slope_angle,temperature_gradient,snow_intensity]]
    prediction=model.predict(input_data)[0]
    if prediction==0:
        msg='No Avalanche!!'
    else:
        msg="Avalanche Imminent!!"
    return render_template('output.html',msg=msg)
    
    

    
    


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)  