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
pip uninstall --yes tensorflow scipy pandas numpy h5py scikit-learn


######################
## install
######################

conda install -y tensorflow scipy pandas numpy h5py scikit-learn

echo "success!!......"