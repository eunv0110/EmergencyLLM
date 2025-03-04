import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
# 2. model prediction------------------
# 데이터 예측 함수
def predict(text ,path ,device='cuda')->int:
    '''
    이 함수는 응급 전화로부터 요약된 문장을 입력받고 이미 학습된 모델이 1,2,3,4,5 등급으로 응급도를 예측하는 모델입니다.
    
    Args:
        - text(Text:str): 요약된 응급 문장
        - model(Any): HuggingFace의 모델
        - tokenizer(Any): HuggingFace의 모델을 따라가는 Tokenizer
        - save_directory(str): 이미 학습된 가중치가 들어있는 pt 파일 경로
        - device (default='cuda') = 'cuda' or 'cpu'
    return:
        - pred(int): 응급 등급 확인 
    '''

    device =torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 토크나이저 로드
    tokenizer = AutoTokenizer.from_pretrained(path)
    
    # 입력 문장 토크나이징
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    inputs = {key: value.to(device) for key, value in inputs.items()}  # 입력 텐서를 GPU로 이동
    model = AutoModelForSequenceClassification.from_pretrained(path)

    # 모델 예측
    with torch.no_grad():
        outputs = model(**inputs)
    # 로짓을 소프트맥스로 변환하여 확률 계산
    logits = outputs.logits
    probabilities = logits.softmax(dim=1)
    # 가장 높은 확률을 가진 클래스 선택
    pred = torch.argmax(probabilities, dim=-1).item()
    return pred