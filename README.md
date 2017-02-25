# Machine Learning Demystified
A weekly workshop series at NYU ITP to teach machine learning with a focus on deep learning

## Week1

### Setup Environment
#### 1) Install miniconda 
   - Go to https://conda.io/miniconda.html 
   - Choose Python 3.6 Mac OSX 64-bit (bash installer) and download
   
#### 2) Open Terminal
   - Type: `cd /path/to/the/file/you/just/downloaded`
   - You can just drag the bash file you download into your terminal window from where you installed it
   - Press `Enter` to continue
   - Review the license and approve the license terms - type in `yes` and press enter
   - Press `Enter` again to confirm the location of install
   - Type `yes` when it asks you if the install location should be prepended to PATH
   - Restart Terminal for changes to take effect
   - Type: `conda info`
   - If it prints out some stuff then it has installed correctly
   
#### 3) Create an environment
   - Open Terminal
   - Type: `conda create -n tensor python=3.5.2`
   - Type: `y` (and press Enter)
   - This will create a conda environment with the name 'tensor' and python version 3.5.2

#### 4) Activate environment
   - Open Terminal
   - Type: `source activate tensor`
   - You should see (tensor) prepended before your terminal prompt

#### 4) Install dependencies
   - Make sure you can see (tensor) prepended before the terminal prompt before proceeding
   - Type: `conda install numpy matplotlib jupyter`
   - Type: `y` (and press Enter)

#### 5) Install Tensor Flow
   - In the same terminal window type: `pip install tensorflow` 
   - If the above command gives an error (it shows up in red color in your terminal **only then** do the following):
     - Type: `pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl`

