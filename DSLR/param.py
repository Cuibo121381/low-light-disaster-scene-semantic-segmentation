################ Hyper Parameters ################
# data Set
dataSetName = '5K_dataset'
dataSetMode = 'test'
dataPath = './data/training/'

maxDataNum = 4500
batchSize = 1

# Crop image size  => 178*356(blur) + 178*356(sharp) = 356*356(crop image)
MaxCropWidth = 1280
MinCropWidth = 0
MaxCropHeight = 720
MinCropHeight = 0

# model
NOF = 64
NOF2 = 32

# train
MaxEpoch = 100
learningRate = 0.00003

# save
numberSaveImage = 20
############################################
