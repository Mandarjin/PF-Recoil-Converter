import typer
import pyperclip
from inspect import cleandoc

entry_points={"console_scripts": ["realpython=reader.__main__:main"]},

app = typer.Typer()


def calc_mean(args) -> float:
    min, max = args
    return (min + max) / 2


def calc_variance(args) -> float:
    mean, min = args
    return round(abs(mean - min), 3)


@app.command()
def convert():
    """Converts recoil from the old PF format to the new COR format"""

    print("PF Recoil Converter V2. Made by @orange., Thanks to @yeha.\n"
          "Input values left to right with a space between them\n"
          "Translational recoil goes X>Y>Z instead of Y>X>Z\n"
          "Weird fuckin inconsitency\n")    

    minCamY, minCamX, minCamZ = minCam = tuple(map(float, input('Min Cam (Y,X,Z): ').split(' ')))
    maxCamY, maxCamX, maxCamZ = maxCam = tuple(map(float, input('Max Cam (Y,X,Z): ').split(' ')))

    minTransX, minTransY, minTransZ = minTrans = tuple(map(float, input('Min Trans (X,Y,Z): ').split(' ')))
    maxTransX, maxTransY, maxTransZ = maxTrans = tuple(map(float, input('Max Trans (X,Y,Z): ').split(' ')))
    
    minRotX, minRotY, minRotZ = minRot = tuple(map(float, input('Min Rot (Y,X,Z): ').split(' ')))
    maxRotX, maxRotY, maxRotZ = maxRot = tuple(map(float, input('Max Rot (Y,X,Z): ').split(' ')))

    groupCamMinAndMax = zip(minCam, maxCam)
    meanCamY, meanCamX, meanCamZ = meanCam = tuple(map(calc_mean, groupCamMinAndMax))
    groupCamMeanAndMin = zip(meanCam, minCam)
    varianceCamY, varianceCamX, varianceCamZ = varianceCam = tuple(map(calc_variance, groupCamMeanAndMin))

    groupTransMinAndMax = zip(minTrans, maxTrans)
    meanTransY, meanTransX, meanTransZ = meanTrans = tuple(map(calc_mean, groupTransMinAndMax))
    groupTransMeanAndMin = zip(meanTrans, minTrans)
    varianceTransY, varianceTransX, varianceTransZ = varianceTrans = tuple(map(calc_variance, groupTransMeanAndMin))
    
    groupRotMinAndMax = zip(minRot, maxRot)
    meanRotY, meanRotX, meanRotZ = meanRot = tuple(map(calc_mean, groupRotMinAndMax))
    groupRotMeanAndMin = zip(meanRot, minRot)
    varianceRotY, varianceRotX, varianceRotZ = varianceRot = tuple(map(calc_variance, groupRotMeanAndMin))


    output = cleandoc(f"""
    Mean, variance Camera Y {meanCamY}, {varianceCamY}
    Mean, variance Camera X {meanCamX}, {varianceCamX}
    Mean, variance Camera Z {meanCamZ}, {varianceCamZ}

    Mean, variance Translational Y {meanTransY}, {varianceTransY}
    Mean, variance Translational X {meanTransX}, {varianceTransX}
    Mean, variance Translational Z {meanTransZ}, {varianceTransZ}

    Mean, variance Rotaional Y {meanRotY}, {varianceRotY}
    Mean, variance Rotaional X {meanRotX}, {varianceRotX}
    Mean, variance Rotaional Z {meanRotZ}, {varianceRotZ}
    """)
    print(output)
    pyperclip.copy(output)
    print('Output copied to clipboard!')

    
@app.command()
def oneliners():
    """the one peice is real"""

if __name__ == '__main__': import pyperclip; (minCam := tuple(map(float, input('Min Cam (Y, X, Z): ').split(' '))), maxCam := tuple(map(float, input('Max Cam (Y, X, Z): ').split(' '))), minTrans := tuple(map(float, input('Min Trans (X, Y, Z): ').split(' '))), maxTrans := tuple(map(float, input('Max Trans (X, Y, Z): ').split(' '))), minRot := tuple(map(float, input('Min Rot (Y, X, Z): ').split(' '))), maxRot := tuple(map(float, input('Max Rot (Y, X, Z): ').split(' '))), meanCam := tuple(map(lambda x: (x[0] + x[1]) / 2, zip(minCam, maxCam))), varianceCam := tuple(map(lambda x: round(abs(x[0] - x[1]), 3), zip(meanCam, minCam))), meanTrans := tuple(map(lambda x: (x[0] + x[1]) / 2, zip(minTrans, maxTrans))), varianceTrans := tuple(map(lambda x: round(abs(x[0] - x[1]), 3), zip(meanTrans, minTrans))), meanRot := tuple(map(lambda x: (x[0] + x[1]) / 2, zip(minRot, maxRot))), varianceRot := tuple(map(lambda x: round(abs(x[0] - x[1]), 3), zip(meanRot, minRot))), output := f"\nMean, variance Camera Y {meanCam[0]}, {varianceCam[0]}\nMean, variance Camera X {meanCam[1]}, {varianceCam[1]}\nMean, variance Camera Z {meanCam[2]}, {varianceCam[2]}\n\nMean, variance Translational Y {meanTrans[0]}, {varianceTrans[0]}\nMean, variance Translational X {meanTrans[1]}, {varianceTrans[1]}\nMean, variance Translational Z {meanTrans[2]}, {varianceTrans[2]}\n\nMean, variance Rotational Y {meanRot[0]}, {varianceRot[0]}\nMean, variance Rotational X {meanRot[1]}, {varianceRot[1]}\nMean, variance Rotational Z {meanRot[2]}, {varianceRot[2]}\n", print(output), pyperclip.copy(output), print('Output copied to clipboard!'))

@app.command()
def hello():
    """Empty command for testing"""
    pass


@app.command()
def info():
    print("This is a PF recoil converter to (hopfully) be accurate with converting old stats to the new ones"
          "Please send any feedback and or issues to @orange. on discord"
          "Version 2.5 Made by @orange., Thanks to @yeha.")


if __name__ == "__main__":
    app()
# trans rights
