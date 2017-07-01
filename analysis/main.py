#!/usr/bin/env python

from sklearn.ensemble import GradientBoostingClassifier
from helpers.data import load_data
from helpers.logger import bot

#bot.debug("Hello, here is a debug message!")
#bot.debug("Hello, here is a warning message!")
#bot.debug("Hello, here is an error message!")
#bot.debug("Hello, here is an info message!")


train = load_data(name="training")


## BUILD MODEL HERE ####################################


# Baseline is provided as an example

variables = ['LifeTime',
             'FlightDistance',
             'pt']

baseline = GradientBoostingClassifier(n_estimators=40, 
                                      learning_rate=0.01, 
                                      subsample=0.7,
                                      min_samples_leaf=10, 
                                      max_depth=7, 
                                      random_state=11)

baseline.fit(train[variables], train['signal'])



# MODEL TESTING ########################################


from metrics import (
    check_agreement,
    check_correlation,
    check_auc
)

agree = check_agreement(baseline,variables)
bot.info("Check Agreement Result:" %agree)
corr = check_correlation(baseline,variables)
bot.info("Check Correlation Result:" %corr)

train_eval = train[train['min_ANNmuon'] > 0.4]
auc = check_auc(baseline,train_eval,variables)
bot.info("Check AUC Result:" %auc)





# DERIVE RESULT FOR TEST ###############################
from helpers.results import save_result


test = load_data(name="test")
result = pandas.DataFrame({'id': test.index})
result['prediction'] = baseline.predict_proba(test[variables])[:, 1]
save_result(result)
