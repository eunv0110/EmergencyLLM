import json
def TextToSummary(input_text, c):
   # OpenAI 클라이언트 생성
  client = c

  # 시스템 역할과 응답 형식 지정
  system_role = '''당신은 응급전화로부터 핵심을 요약하고 응급상황인지 아닌지 판단하는 어시스턴트입니다.
  요약은 최대 20자 이내로 작성하세요. 그리고 증상을 중심으로 요약하세요.
  응답은 다음의 형식을 지켜주세요
  출력예시: {화상 사고로 인해 피부가 심하게 손상되고 통증으로 의식잃은 상태}
  {"summary": \"텍스트 요약\"}
  '''

  # 입력데이터를 GPT-3.5-turbo에 전달하고 답변 받아오기
  response = client.chat.completions.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system",
                                                       "content": system_role},
                                                      {"role": "user",
                                                       "content": input_text} ])

  # 응답 받기
  answer = response.choices[0].message.content


  # 응답형식을 정리하고 return
  answer = json.loads(answer)
  return answer['summary']

  df['summary'] = df[text].apply(answer)