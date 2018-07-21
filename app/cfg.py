# import os
# from pathlib import Path

# from flask import Flask

# app = Flask(__name__)
# debug = 'APP_RELEASE' not in os.environ
# chunk = 1024 * 1024 * 4

# if debug:
#     app.debug = True

# # p = Path(__file__).parent
# # keras_model_path = str(
# #     p / 'neural' / 'snapshots' / 'resnet50_NIKITA_regression_acc_best.h5')
# # neural_labels = {0: "trash", 1: "normal", 2: "2nucl", 3:"micro"}
# # out_img_path = str(p.parent / 'static')
