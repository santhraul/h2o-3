import h2o
from h2o.estimators.glm import H2OGeneralizedLinearEstimator
from h2o.grid.grid_search import H2OGridSearch
h2o.init()
path = h2o.system_file("prostate.csv")
h2o_df = h2o.import_file(path)
h2o_df['CAPSULE'] = h2o_df['CAPSULE'].asfactor()
lambda_opts = [1, 0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0]
hyper_parameters = {"lambda":lambda_opts}


grid = H2OGridSearch(H2OGeneralizedLinearEstimator(family="binomial"), hyper_params=hyper_parameters)
grid.train(y = "CAPSULE", x = ["AGE", "RACE", "PSA", "GLEASON"], training_frame = h2o_df)
for m in grid:
    print "Model ID: " + m.model_id + " auc: " + str(m.auc())
    print m.summary()
    print "\n\n"
