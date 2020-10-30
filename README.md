# Visual Question Answering Visualiser (VQA-VIZ)
An easy-to-use app to visualise attentions of various VQA models.

## Demo
![landing page of vqa-viz](assets/landing.jpg)
![top 7 predictions](assets/predictions.jpg)
![image attentions](assets/img_att.jpg)
![text attentions](assets/text_att.jpg)


• [Requirements](#requirements)  
• [Installation](#installation)  
• [Usage](#usage)  
• [Contributing](#contributing)  
• [Acknowledgements](#acknowledgements)  

## Requirements
Please check the [requirements.txt](https://github.com/apugoneappu/vqa_visualise/blob/master/requirements.txt) file for the version numbers.

1. torchvision
2. seaborn
3. pandas
4. matplotlib
5. dotmap
6. streamlit
7. numpy
8. torch
9. torchvision
10. Pillow
11. PyYAML
12. opencv_python

## Installation
1. Install Anaconda 
2. Clone this repository and cd into it.  
```git clone https://github.com/apugoneappu/vqa_visualise.git && cd vqa_visualise```
3. In a new environment (`new_env`)  
```pip install -r requirements.txt```  

## Usage
From the directory of this repository, do the following -

1. ```conda activate new_env```
2. ```streamlit run vqa_input.py```
3. In a browser tab, open the Network URL displayed in your terminal.

Done! 🎉

## Contributing

First of all, thank you for wanting to contribute to this work! I will try and make your job as easy as possible.

## Acknowledgements 
This repository has been built by modifying the [OpenVQA repository](https://github.com/MILVLG/openvqa/). 

I would also like to thank [Yash Khandelwal](https://github.com/yash12khandelwal), [Nikhil Shah](https://github.com/itsshnik) and [Chinmay Singh](https://github.com/chinmay-singh) for their support and amazing suggestions!

