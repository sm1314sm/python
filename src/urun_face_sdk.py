import base64
from aip import AipFace

""" baidu APPID AK SK """
APP_ID = '22547602'
API_KEY = 'rHVkGHRR8xKwKl5DCzBifYT0'
SECRET_KEY = 'ga0l9ZPk6YSiHrjtPAxAzLzoYKIDQCtQ'
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

flag = 2
if flag == 0:
    # 0 - face detection DEMO
    f = open('data/leaders/test.samples.Leaders3.png', 'rb')
    image = base64.b64encode(f.read())
    image64 = str(image,'utf-8')
    imageType = "BASE64"
    print( client.detect(image64, imageType) )

    options = {}
    options["face_field"] = "age"
    options["max_face_num"] = 10
    options["face_type"] = "LIVE"
    options["liveness_control"] = "LOW"
    print( client.detect(image64, imageType, options) )

elif flag == 1:
    # 1 - face search 1:N DEMO
    f = open('data/leaders/test.samples.Wei.png', 'rb')
    image = base64.b64encode(f.read())
    image64 = str(image,'utf-8')
    imageType = "BASE64"
    groupIdList = "group_repeat"
    print( client.search(str(image64), imageType, groupIdList) )

    options = {}
    options["max_face_num"] = 3
    options["match_threshold"] = 70
    options["quality_control"] = "NORMAL"
    options["liveness_control"] = "LOW"
    options["user_id"] = "233451"
    options["max_user_num"] = 3
    print( client.search(str(image64), imageType, groupIdList, options) )

elif flag == 2:
    # 2 - face search M:N DEMO
    f = open('data/workers/test.samples.Workers.png', 'rb')
    image = base64.b64encode(f.read())
    image64 = str(image,'utf-8')
    imageType = "BASE64"
    groupIdList = "group_2"
    print("Basic")
    print( client.multiSearch(str(image64), imageType, groupIdList) )

    options = {}
    options["max_face_num"] = 10
    options["match_threshold"] = 70
    print("Advanced")
    print( client.multiSearch(str(image64), imageType, groupIdList, options) )
