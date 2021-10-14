"""
 Name: Romeo Garcia, Angela You, Ashwin Deodhar
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: Fall 2021
 Instructor: Dr. Cao
 Date: 10/13/21
 Sources consulted: N/A

 Known Bugs: N/A

 Creativity: N/A

 Instructions: Keep this file, and data.txt in the same directory, and run lab3 in an IDE after
 configuring options for running one of the modes.

"""
import sys
import argparse
import math

def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """
    
    out_train = open(trainData, "w")
    out_test = open(testData, "w")

    with open(data) as file:
        inputList = list(file)  # list of all the lines
        rows = sum(1 for line in file) - 1 #gets rows, does not count header
        row_ratio = int(rows * float(ratio))
        for i in range(row_ratio): #writes to train
            out_train.write(inputList[i + 1])
        for i in range(rows - row_ratio, rows): #writes to test
            out_test.write(inputList[i + 1])
    out_train.close()
    out_test.close()

def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    # your code here
    pass

def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    if mode == "N":
        """
        The normal split mode
        """
        dataFile = options.input
        trainData = options.output1
        testData = options.output2
        ratio = options.ratio
        if dataFile == '' or trainData == '' or testData == '' or ratio == '':
            showHelper()
        
        splitData(dataFile, trainData, testData, ratio)
    elif mode == "R":
        """
        The random split mode
        """
        dataFile = options.input
        trainData = options.output1
        testData = options.output2
        ratio = options.ratio
        if dataFile == '' or trainData == '' or testData == '' or ratio == '':
            showHelper()
        
        splitDataRandom(dataFile, trainData, testData, ratio)
    
def showHelper():
    parser.print_help(sys.stderr)
    print("Please provide input augument. Here are examples:")
    print("python " + sys.argv[0] + " --mode N --input data.txt --output1 TrainingData.txt --output2 TestData.txt --ratio 0.7")
    print("python " + sys.argv[0] + " --mode R --input data.txt --output1 TrainingData.txt --output2 TestRandomData.txt --ratio 0.5")
    
    sys.exit(0)


if __name__ == "__main__":
    #------------------------arguments------------------------------#
    #Shows help to the users                                        #
    #---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode',
    default = '',    # default empty!
    help = 'Mode: R for random splitting, and N for the normal splitting')
    parser.add_argument('--input', dest='input',
    default = '',    # default empty!
    help = 'The input file. Remains the same for both N mode and R mode, being the data file split.')
    parser.add_argument('--output1', dest='output1',
    default = '',    # default empty!
    help = 'The first output file. For both modes this will be the TrainData that is produced.')
    parser.add_argument('--output2', dest='output2',
    default = '',    # default empty!
    help = 'The second output file. For both modes this will be the TestData that is produced.')
    parser.add_argument('--ratio', dest='ratio',
    default = '',    # default empty!
    help = 'The ratio. For both modes this will be what defines how the data is split.')

    if len(sys.argv)<3:
        showHelper()
    main()
