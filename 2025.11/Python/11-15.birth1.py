import datetime
import copy

data={}
month=[]
today=datetime.date.today()
def tuki(year_=datetime.date.today().year):
    month=[35,35,35,35,35,35,35,35,35,35,35,35]
    for i in range(0,12,1):
        while True:
            try:
                datetime.date(year_,i+1,month[i])
                break
            except:
                month[i]-=1
        print("month:",month,";;","month[i]:",month[i])
    return month

def reset() :
    data={}
    today=datetime.date.today()
    tuki()

reset()

def query_stable1(queryText,inputText="ここに入力",errorText="入力が不正です",iferror_returntxt=None,types="int",Repeat=True):
    if types=="int":
        while True:
            print(queryText)
            data["query_1"]=input(inputText)
            try:
                data["query_1"]=int(data["query_1"])
                break
            except:
                print(errorText,":",data["query_1"])
                if Repeat:
                    continue
                else:
                    return iferror_returntxt
        return data["query_1"]
    
def query_stable2(queryText,inputText="ここに入力",errorText="入力が不正です",iferror_returntxt=None,types="int",Repeat=True,max_=None,min_=None):
    if types=="int":
        while True:
            print(queryText)
            try:
                data["query_1"]=input(inputText)
            except:
                data["query_1"]=None
                print("文字列解析エラーです。もう一度入力し直してください。")
                continue

            data["query_1"]=data["query_1"].replace("\n", "")
            data["query_1"]=data["query_1"].replace(" ", "")
            data["query_1"]=data["query_1"].replace("　", "")
            data["query_1"]=data["query_1"].replace("\t", "")
            #int("全角数字")でもPythonは変換してくれる

            try:
                try:
                    data["query_1"]=int(data["query_1"])
                    if (data["query_1"]<=max_ and data["query_1"]>=min_)or(max_==None and min_==None) :
                        break
                    else:
                        print(errorText,":",data["query_1"])
                        if Repeat:
                            continue
                        else:
                            return iferror_returntxt
                except:
                    data["query_1"]=int(data["query_1"])
                    if (max_==None and min_==None):
                        break
                    else:
                        print(errorText,":",data["query_1"])
                        if Repeat:
                            continue
                        else:
                            return iferror_returntxt
                        
            except:
                print(errorText,":",data["query_1"])
                if Repeat:
                    continue
                else:
                    return iferror_returntxt
        return data["query_1"]
    
def query_stable3(queryText,inputText="ここに入力",errorText="入力が不正です",iferror_returntxt=None,types="int",Repeat=True,max_=None,min_=None):
    if types=="int":
        while True:
            print(queryText)
            try:
                data["query_1"]=input(inputText)
            except:
                data["query_1"]=None
                print("文字列解析エラーです。もう一度入力し直してください。")
                continue

            data["query_1"]=data["query_1"].replace("\n", "")
            data["query_1"]=data["query_1"].replace(" ", "")
            data["query_1"]=data["query_1"].replace("　", "")
            data["query_1"]=data["query_1"].replace("\t", "")
            #int("全角数字")でもPythonは変換してくれる

            try:
                try:
                    data["query_1"]=int(data["query_1"])
                    if (data["query_1"]<=max_ and data["query_1"]>=min_)or(max_==None and min_==None) :
                        break
                    else:
                        print(errorText,":",data["query_1"])
                        if Repeat:
                            continue
                        else:
                            return iferror_returntxt
                except:
                    data["query_1"]=int(data["query_1"])
                    if (max_==None and min_==None):
                        break
                    else:
                        print(errorText,":",data["query_1"])
                        if Repeat:
                            continue
                        else:
                            return iferror_returntxt
                        
            except:
                print(errorText,":",data["query_1"])
                if Repeat:
                    continue
                else:
                    return iferror_returntxt
        return data["query_1"]
    

def day_(mode_="stable2") :
    reset()
    if mode_=="stable1":
        #stable(安定版)、通常モード
        data["today"]=datetime.date.today()
        print(f"""\n今日は {datetime.date.today().year}年 {datetime.date.today().month}月 {datetime.date.today().day}日\n""")
        data["year"]=query_stable1("誕生年を入力してください。","ここに入力","入力が不正です。",datetime.date.today().year)
        data["month"]=query_stable1("誕生月を入力してください。","ここに入力","入力が不正です。",datetime.date.today().month)
        data["day"]=query_stable1("誕生'日'を教えてください。◯日の日です。","ここに入力","入力が不正です。",datetime.date.today().day)
    
    if mode_=="stable2" or mode_=="dev1":
        #stable(安定版)v2
        data["today"]=datetime.date.today()
        print(f"""\n今日は {datetime.date.today().year}年 {datetime.date.today().month}月 {datetime.date.today().day}日\n""")
        data["year"]=query_stable2("誕生年を入力してください。","ここに入力","入力が不正です。",datetime.date.today().year,"int",True,datetime.date.today().year,0)
        data["month"]=query_stable2("誕生月を入力してください。","ここに入力","入力が不正です。",datetime.date.today().month,"int",True,12,1)
        data["day"]=query_stable2("誕生'日'を教えてください。◯日の日です。","ここに入力","入力が不正です。",datetime.date.today().day,"int",True,31,1)
        print(f"""{data['year']},{data['month']},{data['day']}""")
        while True:
            try:
                data["birthday"]=datetime.date(data["year"],data["month"],data["day"])
                break
            except:
                data["day"]-=1
        print_system(math_system())

    if mode_=="stable3":
        #dev版(開発中)
        data["today"]=datetime.date.today()
        print(f"""\n今日は {datetime.date.today().year}年 {datetime.date.today().month}月 {datetime.date.today().day}日\n""")
        data["year"]=query_stable3("誕生年を入力してください。","ここに入力","入力が不正です。",datetime.date.today().year,"int",True,datetime.date.today().year,0)
        data["month"]=query_stable3("誕生月を入力してください。","ここに入力","入力が不正です。",datetime.date.today().month,"int",True,12,1)
        data["day"]=query_stable3("誕生'日'を教えてください。◯日の日です。","ここに入力","入力が不正です。",datetime.date.today().day,"int",True,31,1)
        print(f"""{data['year']},{data['month']},{data['day']}""")
        while True:
            try:
                data["birthday"]=datetime.date(data["year"],data["month"],data["day"])
                break
            except:
                data["day"]-=1
        print_system(math_system("stable2"))

def math_system(mode_="stable2"):
    if mode_=="stable1":
        data["life_days"]=(today-data["birthday"]).days
        data["life_week"]=((today-data["birthday"]).days)//7
        return "stable1"
    if mode_=="stable2":
        month=tuki(data["year"])
        data["year_sub"]=data["year"]#年のコピーを作る
        data["life_days"]=(today-data["birthday"]).days
        data["life_days_sub"]=(today-data["birthday"]).days
        data["life_week"]=((today-data["birthday"]).days)//7
        data["life_month"]=0
        i=data["month"]-1
        while True:
            if i==0:
                data["year_sub"]+=1
                month=tuki(data["year_sub"])
            if data["life_days_sub"]-month[i]<0:
                data["month+week+day_week"]=data["life_days_sub"]//7
                data["life_days_sub"]=data["life_days_sub"]%7
                data["month+day_day"]=data["life_days_sub"]
                data["life_year"]=data["life_month"]//12
                break
            else:
                data["life_days_sub"]-=month[i]
                data["life_month"]+=1
                i+=1
                i=i%12
        return "stable2"
    
def print_system(mode_="stable2"):
    if mode_=="stable1":
        #printsystem stable1はmathsystem stable1,dev1,stable2と互換性あり。
        print(data["birthday"],"から",data["today"],"(今日)までの統計(超簡易的)")
        print("生きてきた日数: ",data["life_days"],"日")
        print("生きてきた週数: ",data["life_week"],"週")
    if mode_=="stable2":
        #printsystem stable1はmathsystem stable1,dev1,stable2と互換性あり。
        print(data["birthday"],"から",data["today"],"(今日)までの統計(超簡易的)")
        print("生きてきた日数: ",data["life_days"],"日")
        print("生きてきた週数: ",data["life_week"],"週")
        print("生きてきた月数: ",data["life_month"],"ヶ月")
        print("生きてきた記録: ",data["life_month"],"ヶ月 ",data["month+week+day_week"],"週間 ",data["month+day_day"],"日")
        print("頑張りの勲章。: ",data["life_year"],"年 ",data["life_month"]%12,"ヶ月 ",data["month+week+day_week"],"週間 ",data["month+day_day"],"日")
        print("いつもお疲れさまです。結果だけではなく、その過程も大事なのかもしれませんよ。休憩しながら急がず焦らずがんばってくださいね。")
if input("password")=="dev":
    day_(input("versionを入力"))
else:
    day_()

"""def day_ () :
    today=datetime.date.today()
    while True:
        print("誕生年を入力してください。")
        data["yyyy"]=input("ここに入力")
        try:
            data["yyyy"]=int(data["yyyy"])
            break
        except:
            print("入力が不正です:",data["yyyy"])
            continue
    print("ここに誕生月を入力してください。")
    data["mm"]=int(input("ここに入力"))
day_()"""
