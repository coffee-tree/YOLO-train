# 모델 학습시키기

## Colab에서 실행하는 과정

#### 공식 YOLOv5 레포지토리로 의존성 설정

```jupyter
!git clone https://github.com/ultralytics/yolov5
%cd yolov5
!pip install -r requirements.txt
```

#### 학습 dataset 다운로드

```
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="3Qm4mMrKJ3ziqeMABVyI")
project = rf.workspace("project-fyk0c").project("collection-box")
dataset = project.version(2).download("yolov5")

%mv collection-box-2/ dataset
```

#### 학습 데이터 경로 지정

```
import yaml

# Update the paths in the YAML file to match the new directory structure
with open('dataset/data.yaml', 'r') as f:
    data = yaml.safe_load(f)

# Set the paths directly to the respective directories
data['train'] = 'dataset/train/images'
data['val'] = 'dataset/valid/images'
# If you have a test set, uncomment the following line
# data['test'] = 'dataset/test/images'

with open('dataset/data.yaml', 'w') as f:
    yaml.dump(data, f)

# Verify the updated data
print(data)
```

#### 학습시작 batch epochs 조절 가능

```
!python train.py --img 640 --batch 16 --epochs 50 --data dataset/data.yaml --cfg models/yolov5s.yaml --weights yolov5s.pt --name yolov5s_results
```
