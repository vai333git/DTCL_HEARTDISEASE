import pickle
import json
import config
import numpy as np

# Let's Create Class for Heart Disease Model:
class Heart_Disease():
    # Let's create constructor for creating insatnces of all the variables
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,
                    slope,ca,thal):
                    self.age = age
                    self.sex = sex
                    self.cp = cp
                    self.trestbps = trestbps
                    self.chol = chol
                    self.fbs = fbs
                    self.restecg = restecg
                    self.thalach = thalach
                    self.exang = exang
                    self.oldpeak = oldpeak
                    self.slope = slope
                    self.ca = ca
                    self.thal = thal
    
    def load_models(self):
        print('load model function*************')  
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)
    
    def Get_Disease_Prediction(self):
        self.load_models()

        test_array = np.zeros(len(self.json_data['columns']))

        test_array[0] = self.age
        test_array[1] = self.json_data['sex'][self.sex]
        test_array[2] = self.cp
        test_array[3] = self.trestbps
        test_array[4] = self.chol
        test_array[5] = self.fbs
        test_array[6] = self.restecg
        test_array[7] = self.thalach
        test_array[8] = self.exang
        test_array[9] = self.oldpeak
        test_array[10] = self.slope
        test_array[11] = self.ca
        test_array[12] = self.thal

        print('****************Test_Array is',test_array)
        model_result = str(int(np.around(self.model.predict([test_array]),0)))
        print(model_result,type(model_result),'model_result&*&*&*&*&*&*&*&*&*&*&*&*&*&*&')
        
        disease_predicted = self.json_data['Target'][model_result]

        return disease_predicted

    