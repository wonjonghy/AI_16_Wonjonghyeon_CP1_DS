```
BaseModel
├── results
├── text
├── utils
│   ├── __init__.py
│   └── project.py
└── test.ipynb
```

- model: https://huggingface.co/wjh203/project-cp1/tree/main
- result: project.py로 요약한 결과가 있습니다.
- text: result 요약에 쓰인 텍스트들이 있습니다.
- utils: 요약 모델을 불러오는 모듈인 project 모듈이 있습니다. 모듈 안의 Summary 클래스에는 텍스트 파일을 열고 리스트에 텍스트를 옮기는 stack_txt와 텍스트를 전처리하는 preprocess, 요약 예측을 하는 inference 메서드가 있습니다.

```python
from utils.project import Summary #project.py에 구현된 Summary 클래스를 불러옵니다. 

summary = Summary()
summary.stack_txt('파일 경로') #텍스트 파일 내 텍스트를 리스트에 옮깁니다. summary.text_lst를 통해 리스트를 보실 수 있습니다.
summary.preprocess() #리스트 내 텍스트를 전처리합니다. 마찬가지로 summary.text_lst를 통해 리스트 내 전처리한 텍스트를 보실 수 있습니다.
summary_text = summary.inference() #리스트 내 각 텍스트를 요약하고 그 결과를 리스트로 반환합니다.
```
- test.ipynb: 해당 패키지가 정상적으로 작동하는지 확인하는 test.ipynb 파일을 포함하고 있습니다.
