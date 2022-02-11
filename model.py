# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 19:17:32 2022

@author: Chandramouli
"""


import pandas as  pd

data = (pd.read_excel('TGV_Express_Forecast.xlsx', skiprows=3, sheet_name='Base Data',index_col='DEPARTURE_DATE',parse_dates=True)
        .dropna(how='all',axis=1))
data.index.freq = 'D'

data.info()

data1=data.iloc[:,4:19]
#data1['DEPARTURE_DATE']=data['DEPARTURE_DATE']
#data1.set_index(['DEPARTURE_DATE'], inplace = True)


train_data=data1[(data1.index >= '2017-01-01') & (data1.index < '2018-02-01')]

test_data=data1[(data1.index >= '2018-02-01')]


##150 day prediction
##train data for 150 column prediction
train_data_150=train_data.iloc[:,0].values.reshape(-1, 1)
y_train_150=train_data.iloc[:,1]

from sklearn.ensemble import RandomForestRegressor
model_150=RandomForestRegressor(n_estimators=100, random_state=1)
model_150.fit(train_data_150,y_train_150)

pred_150=model_150.predict(test_data.iloc[0][0:1].values.reshape(1,-1))


##120 day prediction
##train data for 120 column prediction
train_data_120=train_data.iloc[:,0:2]
y_train_120=train_data.iloc[:,2]


from sklearn.ensemble import RandomForestRegressor
model_120=RandomForestRegressor(n_estimators=100, random_state=1)
model_120.fit(train_data_120,y_train_120)

pred_120=model_120.predict(test_data.iloc[0][0:2].values.reshape(1,-1))

a=test_data.iloc[0][0:2].values.reshape(1,-1)


l=['180','150','120','90','75','60','45','30','15','10','7','6','3','2','1']

for i in range(1,15):
        if i==1:
            import pickle
            train=train_data.iloc[:,0].values.reshape(-1, 1)
            y_train=train_data.iloc[:,1]
            from sklearn.ensemble import RandomForestRegressor
            model=RandomForestRegressor(n_estimators=100, random_state=1)
            model.fit(train,y_train)
            filename = 'finalized_model_{0}.pkl'.format(i)
            pickle.dump(model,open(filename,"wb"))
           
        else:
            import pickle
            train=train_data.iloc[:,0:i]
            y_train=train_data.iloc[:,i]
            from sklearn.ensemble import RandomForestRegressor
            model=RandomForestRegressor(n_estimators=100, random_state=1)
            model.fit(train,y_train)
            filename = 'finalized_model_{0}.pkl'.format(i)
            pickle.dump(model,open(filename,"wb"))
         
    
##testing
import joblib
model_14=joblib.load("finalized_model_14.pkl")
test_data.iloc[0][0:14].values.reshape(1,-1)
pred_14=model_14.predict(test_data.iloc[0][0:14].values.reshape(1,-1))


def load_pkl(name):
    model=joblib.load(name)
    return model



model_150=load_pkl("finalized_model_1.pkl")
pred_150=model_150.predict(test_data.iloc[0][0:1].values.reshape(1,-1))

model_120=load_pkl("finalized_model_2.pkl")
pred_120=model_120.predict(test_data.iloc[0][0:2].values.reshape(1,-1))

model_90=load_pkl("finalized_model_3.pkl")
pred_90=model_90.predict(test_data.iloc[0][0:3].values.reshape(1,-1))

model_75=load_pkl("finalized_model_4.pkl")
pred_75=model_75.predict(test_data.iloc[0][0:4].values.reshape(1,-1))

model_60=load_pkl("finalized_model_5.pkl")
pred_60=model_60.predict(test_data.iloc[0][0:5].values.reshape(1,-1))

model_45=load_pkl("finalized_model_6.pkl")
pred_45=model_45.predict(test_data.iloc[0][0:6].values.reshape(1,-1))

model_30=load_pkl("finalized_model_7.pkl")
pred_30=model_30.predict(test_data.iloc[0][0:7].values.reshape(1,-1))

model_15=load_pkl("finalized_model_8.pkl")
pred_15=model_15.predict(test_data.iloc[0][0:8].values.reshape(1,-1))

model_10=load_pkl("finalized_model_9.pkl")
pred_10=model_10.predict(test_data.iloc[0][0:9].values.reshape(1,-1))

model_7=load_pkl("finalized_model_10.pkl")
pred_7=model_7.predict(test_data.iloc[0][0:10].values.reshape(1,-1))

model_6=load_pkl("finalized_model_11.pkl")
pred_6=model_6.predict(test_data.iloc[0][0:11].values.reshape(1,-1))

model_3=load_pkl("finalized_model_12.pkl")
pred_3=model_3.predict(test_data.iloc[0][0:12].values.reshape(1,-1))

model_2=load_pkl("finalized_model_13.pkl")
pred_2=model_2.predict(test_data.iloc[0][0:13].values.reshape(1,-1))


model_1=load_pkl("finalized_model_14.pkl")
pred_1=model_1.predict(test_data.iloc[0][0:14].values.reshape(1,-1))

test_data.iloc[0][0:14].values.reshape(1,-1)



#inp=list(test_data.iloc[0][0:14].values)
#a=inp
#pred_1=model_1.predict([inp])
        
def inference(inp):
    if len(inp)==14:
        model_1=load_pkl("finalized_model_14.pkl")
        pred_1=model_1.predict([inp])
        print(pred_1)
    elif len(inp)==13:
         model_1=load_pkl("finalized_model_13.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
    elif len(inp)==12:
         model_1=load_pkl("finalized_model_12.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
    elif len(inp)==11:
         model_1=load_pkl("finalized_model_11.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
    elif len(inp)==10:
         model_1=load_pkl("finalized_model_10.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
    elif len(inp)==9:
         model_1=load_pkl("finalized_model_9.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
    elif len(inp)==8:
         model_1=load_pkl("finalized_model_8.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
    elif len(inp)==7:
         model_1=load_pkl("finalized_model_7.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
    elif len(inp)==6:
         model_1=load_pkl("finalized_model_6.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
         
    elif len(inp)==5:
         model_1=load_pkl("finalized_model_5.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
         
    elif len(inp)==4:
         model_1=load_pkl("finalized_model_4.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
         
    elif len(inp)==3:
         model_1=load_pkl("finalized_model_3.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
    elif len(inp)==2:
         model_1=load_pkl("finalized_model_2.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
    elif len(inp)==1:
         model_1=load_pkl("finalized_model_1.pkl")
         pred_1=model_1.predict([inp])
         print(pred_1)
        
        

test=[78]

inference(test)   


test=[78,98]
inference(test)    


test=[26,34,57,97,110,142,164,203,221,240,271,275,281,286]
inference(test)    


test=[15,21,26,32,34,51,171,279,279,355]
inference(test)    


