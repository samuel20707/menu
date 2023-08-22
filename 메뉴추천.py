import discord
import asyncio
import random
import datetime
from datetime import datetime


intents = discord.Intents.all()
client = discord.Client(intents=intents)


Botname = '봇이름'
token = '봇토큰'

menu_list = ["짜장면", "피자", "치킨", "초밥", "떡볶이", "삼겹살", "우동", "라면", "물냉면", "비빔밥", "삼겹살", "된장찌개", "불고기", "잡채밥", "김치찌개", "갈비탕", "떡볶이", "소고기볶음밥", "해물파전", "쭈꾸미볶음", "감자탕", "산채비빔밥", "산낙지", "칼국수", "샤브샤브", "육회", "회덮밥", "김밥", "라면", "우동", "초밥", "돈부리", "참치회", "샐러드", "파스타", "스테이크", "그라탕", "치킨스테이크", "수제피자", "중화볶음밥", "탕수육", "짬뽕", "군만두", "삼선짜장", "매운탕", "홍합탕", "카레라이스", "소세지야채볶음", "양념치킨", "베이컨감자튀김", "케이준치킨", "양꼬치", "짜조면", "만두국", "부대찌개", "해물탕", "닭볶음탕", "순대국", "냉모밀", "오므라이스", "햄버거", "산적비빔밥", "오리주물럭", "홍어회", "산낙지숙회", "장어구이", "돼지국밥", "물회", "곰탕", "산채조림", "고등어조림", "황태해장국", "갈비찜", "닭갈비", "산적국수", "해물누룽지탕", "생선구이", "돈까스", "오므라이스", "오코노미야키", "모밀", "팟타이", "빈대떡", "호떡", "삼각김밥", "임실치즈국밥", "두부조림", "양념게장", "매운막창", "돼지껍데기", "곱창구이", "뼈해장국", "감자전", "미역국", "닭볶음", "팔보채", "돼지꽃게탕", "토란국", "계란국", "비빔국수", "팥빙수", "인절미빙수", "팥죽", "녹차빙수", "왕만두", "찹쌀떡", "호박전", "야채전", "해물파스타", "삼겹살김치찜", "등갈비찜", "미나리전", "장어덮밥", "치즈라면", "매운갈비찜", "오리불고기", "동태찌개", "고등어구이", "오꼬노미야끼", "육전", "육개장", "닭곰탕", "북어국", "감자탕", "미역줄기볶음", "목살스테이크", "낙지볶음", "돈코츠라멘", "닭도리탕", "훠궈", "훈제오리", "고추잡채", "보쌈", "전복죽", "해물죽", "콩국수", "참나물고기전", "어묵국", "옛날돈까스", "코다리조림", "부대전골", "쌀국수"]
recommended_menu = random.choice(menu_list)

@ client.event
async def on_ready():
    print(f'{Botname}이 켜졌습니다.')
    print('-----------------------------------------------------------------------')
    print(f"[!] 참가 중인 서버 : {len(client.guilds)}개의 서버에 참여 중")
    print(f"[!] 서버 인원 총합 : {len(client.users)}와 함께하는 중")
    print('-----------------------------------------------------------------------')
    guild_list = client.guilds
    for i in guild_list:
        print("서버 ID: {} / 서버 이름: {} / 멤버 수: {}".format(i.id, i.name, i.member_count))
    print('-----------------------------------------------------------------------')
    now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    print(f'TIME: [ {now} ] / BOT IS ONLINE')
    while True:
        await asyncio.sleep(600)
        now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        print(f'TIME: [ {now} ] / BOT IS ONLINE')

@ client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content==('!메뉴추천'):
        recommended_menu = random.choice(menu_list)
        await message.reply('오늘은 {} 어떠세요?'.format(recommended_menu))


client.run(token)