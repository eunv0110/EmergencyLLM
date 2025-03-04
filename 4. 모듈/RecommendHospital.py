from GetDistance import GetDistance
import pandas as pd
# 3-2. recommendation------------------
def RecommandHospital(my_location, df):
    my_lat, my_lon = my_location
    alpha = 0
    df_temp = pd.DataFrame()

    while len(df_temp) < 3:
        alpha += 0.1
        lat_min, lat_max = my_lat - alpha, my_lat + alpha
        lon_min, lon_max = my_lon - alpha, my_lon + alpha
        df_temp = df[(df['위도'] >= lat_min) & (df['위도'] <= lat_max) &
                     (df['경도'] >= lon_min) & (df['경도'] <= lon_max)].copy()

    distances = []
    times = []
    for index in range(len(df_temp)):
        hospital_lat = df_temp.iloc[index]['위도']
        hospital_lon = df_temp.iloc[index]['경도']

        # `GetDistance`로 도로 거리 및 소요 시간 계산
        distance, time = GetDistance(my_lat, my_lon, hospital_lat, hospital_lon)
        distances.append(distance)
        times.append(time)

    # 계산한 도로 거리 및 소요 시간 추가
    df_temp['거리(km)'] = distances
    df_temp['소요시간(분)'] = times

    # 거리 기준으로 정렬
    df_temp = df_temp.sort_values(by='거리(km)', ascending=True).reset_index(drop=True)

    # 가장 가까운 병원 3곳 반환
    return df_temp[:3]