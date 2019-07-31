# from life import Life
class Life:
    tema = [["1.교무실에서","2.교실에서"],  #학교에서
        [None,None,None],  #회사에서
        ["패스트푸드점에서","쇼핑할때","대중교통을 이용할때"],          #공공장소
        [None,None,None]]                                                        #일상생활에서

    tema_Of = ["1.뭐하고 지냈어\
                2.가끔 만나고 지내자\
                3.안녕, 오랜만이야\
                4. 바빠 죽겠어."]
#일상생활에서 자주 쓰는 말들
#1번 번역하고 2번 번역하고 등등 
    sc_of_1lang = ["[뭐하고 지냈어] \n 영어: What have you been up to?(왓 해브 유 빈 업 투) \n \
    중국어: 做什么过(푸어 샹 마 그어)\n \
    일본어: 何して過ごしたの(나니 시테 스고시타노)\n \
    스페인어: ¿Qué has hecho?(큐아세츄)\n \
    프랑스어: Qu'est-ce que tu as fait ?(케스큐 츄에 펫?)",
        "[가끔 만나고 지내자 ] \n   영어: Let's meet once in a while.(렛스 밋 원스 인 어 와일)\n \
        중국어: 偶尔见面吧(오 알 치엔 밍 빠)\n \
        일본어: たまには会って過ごそう(타마니와 앗테 스고소오)\n \
        스페인어: Nos vemos de vez en cuando.(노스 베모스 데 벵 덴꼬안노)\n \
        프랑스어: On se voit de temps en temps.(온 스 부앗도 돔 송 통) ",
        "[안녕, 오랜만이야] \n  영어: Hi, long time no see. (하이 롱 타임 노우 시)\n \
        중국어: 嗨,好久不见了,我真想你了(하이 하우 치오 붕 취엔 라 워 쯩 시앙니라)\n \
        일본어: こんにちは,久しぶりだね(콘니치와 히사시부리다네)\n \
        스페인어: Hola, ha pasado mucho tiempo.(올라 아빠 무체 시엔포)\n \
        프랑스어:Bonjour, ça fait longtemps.(봉쥬르 셰피 롱 뎀프)",
            "[바빠 죽겠어 ]\n    영어: I'm so busy. (아임 소우 비지)\n \
        중국어: 忙死了 (망 쓸라)\n \
        일본어: 忙しくてたまらない(이송가시쿠테 타마라나이)\n \
        스페인어: Estoy ocupada.(에이스띠오 꾸 빠라)\n \
        프랑스어: Je suis occupé. Je meurs.(쥬 시어 큐핏 쥼마)"]
#여기서부터 제대로 실행을 하기 때문에 run이라는 함수를 만들었다.

    def run(self,User_S):

        life = Life.tema[int(User_S)-1]   
#일상생활라는 변수를 만들고 tema에 있는 문장들을 User_S가 선택한것들이 들어감.
        for i in Life.tema_Of:                    
            print(i,"\t",end="")
        print()
#for문으로 그 선택한 테마?의 표현들을  하나씩 뽑음 
        User = input("한번더 선택해 주세요")   
        #한번 더 선택
        print(Life.sc_of_1lang[int(User)-1])     
# 마지막 선택에서의 표현들이 출력된다.


        print()