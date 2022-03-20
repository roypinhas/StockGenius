import pickle
class PredictPrice:


    #does not work
    def predict_price(self, symbol, date):
        print("s" + str(symbol))
        print("d" + str(date))
        # load the model from disk
        #loaded_model = pickle.load(open(symbol.upper() + 'model.pkl', 'rb'))
        #prediction = loaded_model.predict(date)
        return 1




