#######################################
#
#
#	SCRIPT PARA ACTUALIZAR
#		TENSORFLOW
#
#
########################################


######################
## uninstall
######################
pip uninstall --yes tensorflow scipy numpy h5py scikit-learn


######################
## install
######################

conda install -y tensorflow scipy numpy h5py scikit-learn

######################
## test
######################

text="import numpy as np
print np.add(1,2)
import tensorflow as tf
print tf.VERSION
import scipy as sp
print sp._version_
"

echo "$text" > test.py

python test.py

rm test.py

echo "success"