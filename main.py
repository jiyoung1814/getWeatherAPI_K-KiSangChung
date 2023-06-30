import requests
from datetime import datetime, timedelta

def setDuration(start_day, end_day):
    start = datetime.strptime(start_day, "%Y-%m-%d")
    end = datetime.strptime(end_day, "%Y-%m-%d")
    diff = [(start + timedelta(days=i)).strftime("%Y%m%d") for i in range((end - start).days + 1)]
    return diff

if __name__ == '__main__':

    #기간 설정
    start_day = '2020-12-29'
    end_day = '2020-12-31'
    dates = setDuration(start_day, end_day)
    url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?"
    serviceKey = '9O7j2l7zOtMPpHHYFDyZxWMEOADIThbUsJODe02VmIMCKwYXRtkFOmOrtITnJfmRU88J4ajcKEvnP%2FefJpy8Tg%3D%3D'
    numOfRows = '10'
    pageNo = '1'
    dataType = 'JSON' #응답 자료 형식(XML, JSON)
    dataCd = 'ASOS' #자료 코드
    dateCd = 'DAY' #날짜 코드
    stnIds = '232' #천안 지점 번호

    # dates = [
    #     # "20210102", "20210106", "20210108", "20210114", "20210119", "20210129", "20210208", "20210212", "20210213", "20210219", "20210221", "20210223", "20210225", "20210226", "20210301", "20210304", "20210305", "20210310", "20210312", "20210316", "20210317", "20210323", "20210325", "20210330", "20210405", "20210407", "20210408", "20210409", "20210411", "20210412", "20210414", "20210419", "20210425", "20210503", "20210509", "20210823", "20211017", "20211116", "20211127", "20211205", "20211207", "20211208", "20211222",
    #     # "20200102", "20200105", "20200118", "20200220", "20200223", "20200308", "20200312", "20200318", "20200320", "20200323", "20200324", "20200401", "20200405","20200408", "20200414", "20200424","20200428", "20200429", "20200712", "20200714", "20200722", "20200906", "20200912","20201008", "20201023", "20201024", "20201030", "20201104", "20201110", "20201112", "20201208", "20201212", "20201214", "20201215", "20201216", "20201217", "20201219", "20201220",
    #     # "20220116", "20220118", "20220120", "20220121", "20220210", "20220217", "20220223", "20220227", "20220303", "20220305", "20220306", "20220317", "20220322",
    #     "20220325", "20220329", "20220403", "20220404", "20220405", "20220527", "20220528", "20220531", "20220605", "20220731", "20220808", "20220904", "20220913", "20220921", "20220927", "20220929", "20220930", "20221012", "20221013", "20221018", "20221211", "20221224", "20221227"
    # ]
    for d in dates:
        startDt = d
        endDt = d
        response = requests.get(url+'serviceKey=' + serviceKey +'&numOfRows=' + numOfRows +'&pageNo=' + pageNo +'&dataType=' + dataType +'&dataCd=' + dataCd +'&dateCd=' + dateCd +'&startDt=' + startDt +'&endDt=' + endDt +'&stnIds=' + stnIds)
        # print(url+'serviceKey=' + serviceKey +'&numOfRows=' + numOfRows +'&pageNo=' + pageNo +'&dataType=' + dataType +'&dataCd=' + dataCd +'&dateCd=' + dateCd +'&startDt=' + startDt +'&endDt=' + endDt +'&stnIds=' + stnIds)

        try:
            print(d+": "+str(response.json()['response']['body']['items']['item'][0]['avgTca']))
        except:
            print(response.json())