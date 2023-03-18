```
BaseModel
├── model
│   ├── .gitattributes
│   ├── config.json
│   ├── pytorch_model.bin
│   ├── special_tokens_map.json
│   ├── tokenizer_config.json
│   └── tokenizer.json
├── results
├── text
├── utils
│   ├── __init__.py
│   └── project.py
└── test.ipynb
```
- model: 요약모델과 토크나이저의 가중치 파일이 있습니다.
- result: project.py로 요약한 결과가 있습니다.
- text: result 요약에 쓰인 텍스트들이 있습니다.
- utils: 요약 모델을 불러오는 모듈인 project 모듈이 있습니다. 모듈 안의 Summary 클래스에는 텍스트 파일을 여는 open_txt와 텍스트를 전처리하는 preprocess, 요약 예측을 하는 inference 메서드가 있습니다.
```python
from utils.project import Summary #project.py에 구현된 Summary 클래스를 불러옵니다. 

summary = Summary()
text = summary.open_txt('파일 경로') #텍스트 파일을 불러옵니다.
preprocessed_text = summary.preprocess(text) #전처리한 텍스트를 반환합니다.
summary.inference(preprocessed_text) #요약한 텍스트를 반환합니다.
```
- test.ipynb: 해당 패키지가 정상적으로 작동하는지 확인하는 test.ipynb 파일을 포함하고 있습니다.