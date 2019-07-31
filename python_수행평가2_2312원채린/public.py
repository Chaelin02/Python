from school import School

class Public:
    tema = [["1.교무실에서","2.교실에서"],  #학교에서
        [None,None,None],  #회사에서
        ["1.패스트푸드점에서","2.쇼핑할때","3.대중교통을 이용할때"],          #공공장소
        [None,None,None]]                                                        #일상생활에서

    tema_go = ["1.제일 잘 팔리는게 뭐에요?\
                2.이거 주세요\
                3.이거는 빼주세요.\
                4.현금 영수증 해주세요." , 
                "1.다른 사이즈 없나요? \
                2.좀 더 둘러보고 올게요\
                3.이걸로 주세요.\
                4.카드(현금)으로 할게요.",
                "1.청소년 한 명이요\
                2.몇 번 출구에요?\
                3.여기로 가주세요.\
                4.거스름돈 주세요."]


    sc_go_1lang = ["[제일 잘 팔리는게 뭐에요?] \n <영어> - What is the most popular menu?(왓 이즈 더 모스트 파퓰러 메뉴) \n \
    <일본어> -一番人気のあるメニューは何ですか。(이치반닌키노 아루 메뉴우와 난데스카) \n \
    <프랑스어> -Quel est le menu le plus populaire ? (낄리 류무니르 프리퓨 플레아)\n \
    <중국어> -最受欢迎的菜是什么？ (트이쇼 화이응다 촤이 슈 샴마)\n \
    <스페인어> - ¿Cuál es el menú más popular? (꽐리 슈르메 노 마미 슈 뿌라르)",
        "[이거 주세요] \n<영어> - Give me this.(기브 미 디스)\n \
        <일본어> - これをください。 (코레오 쿠다사이)\n \
        <프랑스어> - Donnez-moi ça, s'il vous plaît. (도니모와사 시리부 푸에)\n \
        <중국어> - 请给我这个。(치응 테이 워쯔워 거)\n \
        <스페인어> -Dame esto. (다메 예시토)",
        "[이거는 빼주세요] \n <영어> - Please leave this out. (플리즈 리브 디스 아웃)\n \
            <일본어> -これは抜いてください。 (코레와 누이테쿠다사이)\n \
            <프랑스어> - Enlevez-moi ça.(올리 디 모아사) \n \
            중국어> - :这个给我拔拔吧 ( 쯔그 그이워 빠이바 바\n \
            <스페인어> - Sáqueme esto. (사켐메 에시토)",
            "[현금 영수증 해주세요]\n <영어> - I'd like a cash receipt, please. (아이드 라익 어 캐쉬 리싯 플리즈)\n \
                <일본어> -現金領収書をお願いします。 (겐킨료오 슈우쇼오 오네가이시마스)\n \
                <프랑스어> -Un reçu en espèce, s'il vous plaît.(어 구 시온 니스펠스 시 부 플렛)\n \
                <중국어> -请给我现金收据。(즈앙 케이 워 씨엉 즈 쇼우 즈)\n \
                <스페인어> - ¿Podría darme el recibo?(포들리알라 가르멜마라 드르 디보우)"]

    sc_go_2lang = ["[다른 사이즈 없나요?] \n \
    <영어> -Do you have another size? (두유 해브 어나더 사이즈?)\n \
    <일본어> -他のサイズはないですか。(호카노 사이즈와 나이데스키) \n \
    <중국어> - 没有别的尺码吗?(메이요 비에더 취 마 빠)\n \
    <스페인어> -¿No hay otra talla?(노 아이노 트레타이 야) \n \
    <프랑스어> -Vous n'avez pas d'autre chose ? (부네비 파도토 슈스) ",
        "[좀 더 둘러보고 올게요]  \n 영어 : I'll look around and come back.(아일 룩 어라운드 앤드 컴 백) \n \
        일본어: もう少し見てきます。(모오 스코시 미테키마스)\n \
        중국어: 我再转转就来。(워 짜이 쯩 쫘이 증 랑 ) \n \
        프랑스어:Je vais jeter un coup d'oeil. Je reviendrai.(주 비 쥬티앙 코드아이 줘그 졍 트카이)\n \
        스페인어: Voy a mirar un poco más.(보이 아 미레로 봉코 마스)",
        "[이걸로 주세요]  \n 영어 :Give me this.(기브 미 디스) \n \
        일본어:これをください。 (코레오 쿠다사이)\n \
        중국어: 请给我这个。(치응 테이 워쯔워 거)\n \
        프랑스어:Donnez-moi ça, s'il vous plaît. (도니모와사 시리부 푸에) \n \
        스페인어: Dame esto. (다메 예시토)",
        "[카드(현금)으로 할게요.]  \n 영어 : I'd like to use a card (cash).(아이드 라익 투 유즈 어 카아드 캐쉬)\n \
        일본어:現金(げんきん)にします。(겐킨 (겐킨니) 시마스) \n \
        중국어: 我要卡(现金)。(월러 카) \n \
        프랑스어: Je prendrai votre carte. (즈 퍼블리타 큐캬우트) \n \
        스페인어:Tarjeta.(따라 켓타)"]

    sc_go_3lang = ["[청소년이요] \n \
    <영어> Juvenile.(주버널)\n \
    <일본어> -青少年二世(세에쇼오넨 니세에)\n \
    <중국어> - 青少年( 칭 샤오 니응)\n \
    <스페인어> -La adolescencia.(네 아도레스넨시아)\n \
    <프랑스어> -La jeunesse.(레쥬네스)",
        "[몇 번 출구에요?]  \n \
        영어: Which exit is it?(위치 엑싯 이즈 잇)\n \
        중국어: 在几号出口?(싸이 치 하우 추 카우)\n \
        일본어: 何番出口ですか。(난반 데구치데스카)\n \
        스페인어: ¿Cuál es la salida?(꽐리 씰라 살 리이다)\n \
        프랑스어: Quelle porte est-ce ?(켈리 폴트 이스)",
        "[여기로 가주세요]  \n \
        영어: Please take me to this place.(플리즈 테익 미 투 디스 플레이스) \n \
        중국어: 请到这里。(췽 따오 칑리)\n \
        일본어: ここに行ってください。(코코니 잇테쿠다사이)\n \
        스페인어: Por favor, venga aquí.(포르 파보르 벵가아키)\n \
        프랑스어: Allez-y.(알리 지)",
        "[거스름돈 주세요.]  \n \
    영어: Give me the change.(기브 미 더 체인지)\n \
    중국어: 请给我找零钱。(치응 텐 워 짜오르 치안)\n \
    일본어: おつりをください(오츠리토 쿠다사이)\n \
    스페인어: Dame la vuelta(다메 라 부엔타)\n \
    프랑스어: Donnez-moi la monnaie.(두니 모나 모리)\n "]
    def run(self,User_S):
            # for start
      #  User_S = input("알고싶은 표현을 선택하세요")  

        school = Public.tema[int(User_S)-1]    

        for i in school:                    
            print(i,"\t",end="")
        print()
        User = input("한번더 선택해 주세요")   
        if int(User) == 1:
            User_g = input(Public.tema_go[int(User)-1])        
            print(Public.sc_go_1lang[int(User_g)-1])     
        elif int(User) == 2:
            User_g2 = input(Public.tema_go[int(User)-1])       
            print(Public.sc_go_2lang[int(User_g2)-1])     
        elif int(User) == 3:
            User_g3 = input(Public.tema_go[int(User)-1])       
            print(Public.sc_go_3lang[int(User_g3)-1])     


        print()