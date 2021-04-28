# Prediction Model for HLHS

This repository contains models to predict fatality in patients with single left ventricle heart defects, specifically hypoplastic left heart syndrome (HLHS).

HLHS affects one out of 5,000 newborns. The Norwood procedure is the most widely used treatment options for HLHS, yet it remains the opertation with the highest 
risk during staged repair. In order to combat this high mortality rate, I create four predictive models (logistic regression, random forest, support vector machine, 
and neural network models) to classify the probability of mortality for a patient undergoing the Norwood procedure.

The database I used is the Pediatric Heart Network's Single Ventricle Reconstruction (SVR) trial. It is open-source and can be found at 
https://www.pediatricheartnetwork.org/public-use-data-sets.

To run the program, simply clone the repository and run the following commands:

	cd prediction-model-HLHS
	cd models
	python combined.py
