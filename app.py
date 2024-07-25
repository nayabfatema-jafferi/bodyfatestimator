from flask import Flask, render_template,request
import pickle

app = Flask(__name__)

file1 = open('bodyfatmodel2.pkl','rb')
rf = pickle.load(file1)
file1.close()


'''here the forms gets the message that is method is post... and it takes it to this action page where route is /'''
'''i.e whatever data we enter in form gets posted to a service which has url of /'''

@app.route('/', methods = ['GET','POST'])
def Predict():
    if request.method == 'POST':
        est_dict = request.form
        print(est_dict)

        density = float(est_dict['density'])
        hip = float(est_dict['hip'])
        chest = float(est_dict['chest'])
        abdomen = float(est_dict['abdomen'])
        weight = float(est_dict['weight'])
        

        #the data entered is passed as a list of dictionary, with key values as names of variable.. hence to extract that we use list of list with variable names
        input_data = [[density,hip,chest,abdomen,weight]]
        ans = rf.predict(input_data)[0].round(2) #ans is displayed in the form of list.. hence we take the value only.. so [0]and round

        #then we take this answer and put it in another template called show.html
        string = 'Percentage of BodyFat is ' + str(ans) +'%'
        return render_template('show.html', string = string)

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)