# KeLoss Network
## Request classification + word2vec for ranging.
### What it could be..?
Here you will find out scripts for:
* Make VK dataset
* Train Keras model, which we`ve used
* Make prediction by saved model
We have wrote some "libraries" for python. These scripts can be imported as libs and used for more comfotrable data making, training, predicting...
#### Something about parameters..?
Yeah, it could be interesting. We have wrote them for interestiong project.
With standart configuration neural network can give to you nearly 92% accuracy. We have got such accuracy ;)
By default, netwotk has something about 1,506,000 trainable params.
This net is very simple, but it really workd fine for uor project:)
### What do I need to use these scripts?
#### * First, you have to install some python libs by "pip"
* Keras
* pymorphy2 with pymorphy2-dicts-ru/uk (for lemmatization)
* nltk with basic dictionaries (used for stop-words removing)
* numpy
* pandas (dataframes)
* Sci-kit learn (tfidf and pickle)
* pickle (if not implemented by sklearn)

#### * Then tou could make dataset, possibly with our scripts, stored in this branch
#### * Now you can train your own model
#### * And after all, PREDICT THEM ALL!!!
