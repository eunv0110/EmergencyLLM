import requests
# 3-1. get_distance------------------
def GetDistance(start_lat, start_lng, dest_lat, dest_lng):
    url = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving"
    c_id = "5rpillllni"
    c_key = "2fsukZsIpH48SFzlZ8v0GoJ7fXTkiMO3eHJcge12"
    headers = {
        "X-NCP-APIGW-API-KEY-ID": c_id,
        "X-NCP-APIGW-API-KEY": c_key,
    }
    params = {
        "start": f"{start_lng},{start_lat}",  # 출발지 (경도, 위도)
        "goal": f"{dest_lng},{dest_lat}",     # 목적지 (경도, 위도)
        "option": "trafast"                   # 실시간 빠른 길 옵션
    }

    # 요청하고, 답변 받아오기
    response = requests.get(url, params=params, headers=headers)

    # 성공적으로 받아왔다면
    if (response.status_code == 200):
        response_data = response.json()  # JSON 데이터를 파싱
        if response_data["code"] == 0:
            # 거리
            dist = response_data['route']['trafast'][0]['summary']['distance'] / 1000   # km
            # 소요 시간
            time = response_data['route']['trafast'][0]['summary']['duration'] / 60000  # minute
            return round(dist,2), round(time,2)
        else:
            print(f"에러 : {response_data['code']}, {response_data['message']}")
            return None
    else:
        print(f"에러 : {response.status_code}, {response.text}")
        return None