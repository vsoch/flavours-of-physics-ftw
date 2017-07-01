# Mu Tau Tau Tau ContainersFTW

This is a competition orginally [hosted on Kaggle](https://www.kaggle.com/c/flavours-of-physics/data), reproduced here to encourage containerization of submissions by way of [Singularity](https://singularity.lbl.gov). If you aren't familiar with Singularity, it's a container (like Docker) that can be run securely on HPC architectures.


## Competition Overview

1. **Goals**: Read about the [data](https://www.kaggle.com/c/flavours-of-physics/data) to get a breakdown of the data provided, and the [background and goals](https://www.kaggle.com/c/flavours-of-physics) of the competition is beautifully described and shown on Kaggle. 
2. **Build**: Build your container (see build section below), which will install dependencies and prepare data for you. If you find that you need any more, or any additional software or libraries, you can add them to the `%post` section of the [Singularity](Singularity) file.
3. **Code**: Once you have your container built, you can use it to develop and test your submission.
4. **Submit**: A submission to the competition means submitting a PR (pull request)

### Goals
Evaluation for this competition is based on AUC (area under the curve), defined as area under the curve, which broadly gets at the ratio of false positives to false negatives for your model.  In addition to this criteria, the [metrics](metrics.py) file includes multiple checks that physicists do to make sure that results are unbiased.


## Build
When you are ready to start your submission, you should fork the repo to your branch, and then clone the fork. For example, if my username on Github was `vsoch`, I would fork and then do:

```
git clone https://www.github.com/vsoch/flavours-of-physics-ftw
cd flavours-of-physics-ftw
```

Then you can build your image. You will need one dependency, that [Singularity is installed](https://singularityware.github.io). Building comes down to creating an image and then using `bootstrap` to build from the container recipe, [Singularity](Singularity).

```
singularity create --size 8000 container.ftw 
sudo singularity bootstrap container.ftw Singularity
```

## Work in your Container
To shell into your container, you will want to mount the analysis folder, and the external data. You can do that like this. Note that we are making the present working directory (`pwd`) our folder with analysis scripts:

```
singularity shell -B data/input:/data/input -B analysis:/code --pwd /code container.ftw
```

When you shell into your container, it probably will look the same, but if you do `ls /` you will see a file called `singularity` and root folders `/data` and `/code` that aren't on your host. If you look inside, you will see the data and 
analysis scripts mounted!

```
ls /code
README.md  helpers  main.py  metrics.py  results  tests
```

Try creating a file on the host, and you will see it change in the container, or vice versa. Thus, your general workflow will be the following:

 - run things from within the container, using the python or ipython located at `/opt/conda/bin`
 - edit code in your editor of choice on your host machine

### Environment
If you want to ever find data or results locations, these have been provided for you via environment variables:

 - `CONTAINERSFTW_DATA`: The base folder with data
 - `CONTAINERSFTW_RESULT`: The folder where results are written to
 - `CONTAINERSFTW_WORK`: The folder where your scripts live.

It's definitely a good idea if you are interested to shell around the container to understand where things are located, and test the variables to confirm they are the same:

```
echo $CONT
$CONTAINERSFTW_RESULT   $CONTAINERSFTW_DATA     $CONTAINERSFTW_WORK     
echo $CONTAINERSFTW_DATA
/data/input
```

### Code
You can work from inside the container, or comfortable from the host in the `analysis` folder (mapped to `/code` in the container). Your main work is going to be located at `/code/main.py` in the container, which is `analysis/main.py` on the host. If you open up this file, you can start interactively working in an ipython terminal in the container to test commands. For example, from `/code` let's try loading the data in `ipython`

```
from sklearn.ensemble import GradientBoostingClassifier
from helpers.data import load_data
from helpers.logger import bot

train = load_data(name="training")

Valid datasets include:
DEBUG training : /data/input/training.csv
DEBUG test : /data/input/test.csv
DEBUG check_agreement : /data/input/check_agreement.csv
DEBUG check_correlation : /data/input/check_correlation.csv
```


### Adding Dependencies
If you add dependencies (another python module, additional data that conforms to competition rules, etc) you should update the Singularity recipe, for example, we have marked in `%post` where you can add installation steps:

```
     #########################################################
     # Install additional software / libraries here
     #########################################################

     pip install -y pokemon

     #########################################################
```

## FAQ

1. **Do I have to use Python?**: Of course not! The base template image given to use is based on a choice by the creator (for example, lots of people use `scikit-learn` in python for machine learning). At the end of the day, the evaluation is done over the text file in `/analysis/results/submission` and is ambivalent to how it is generated. Your submission (the container image) must simply run to generate it, and you are good.

For now, for additional FAQ please see our [documentation](https://containers-ftw.github.io)
