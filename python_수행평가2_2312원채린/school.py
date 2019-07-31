# from life import Life

class School:
    _tema = [["1.교무실에서","2.교실에서"],  #학교에서
        [None,None,None],  #회사에서
        ["패스트푸드점에서","쇼핑할때","대중교통을 이용할때"],          #공공장소
        [None,None,None]]                                                        #일상생활에서

    _tema_go = ["1.선생님 여쭈어볼게 있어요\
                2.들어가도 될까요?\
                3.선생님 계신가요?\
                4.안녕히계세요" , 
                "1.문 좀 닫아줘 \
                2.이것 좀 주워주라\
                3.다음 과목이 뭐야?\
                4.조용히 좀 해주라"]  #학교에서를 골랐을때 1.교무실에서 2.교실에서로 나뉜 다음 선택하는문장들


    _sc_go_1lang = ["[선생님 여쭈어 볼게 있어요] \n <영어> - I need to ask you something.(아이 니드 투 에스크 유 섬띵) \n \
    <일본어> - 先生,聞きたいことがあります。(센세이 키키타이 코토가 아리마스)\n \
    <프랑스어> -J'ai une question.(주에잉 퀘스치용)\n \
    <중국어> -老师,我有话要说。(라오쉬 워요 화야우 슈어)\n \
    <스페인어> - Profesor, tengo algo que preguntar.(프로프소어 텡고 아르고 쿠 프레공타ㄹ)",
        "[들어가도 될까요?] \n<영어> - May I come in? (메이 아이 컴 인)\n \
        <일본어> - 入ってもいいですか。(하잇 테모 이이데스카)\n \
        <프랑스어> -Est-ce que je peux entrer?(에스 츠 크 쥬 푸쉉 엔트위?)\n \
        <중국어> - 我可以进去吗？ (워커이 이친 슈마)\n \
        <스페인어> - Puedo entrar? (푸에도 엔트롸)",
        "[선생님 계신가요?] \n <영어> - Is there a teacher? (이즈 데얼 어 티쳘?)\n \
            <일본어> - 先生いらっしゃいますか? (센세이 이랏샤이 마스카?)\n \
            <프랑스어> - Y a-t-il un professeur ?(이 가잇 겟 틸 언 프로페서) \n \
            중국어> - 有老师吗?(요 라우 쉬 마)\n \
            <스페인어> - ¿Está el profesor adentro? (이스타렐  프로페쇼 러어덴트롤)",
            "[안녕히계세요]\n <영어> - Goodbye.(굳 바이)\n \
                <일본어> - お気をつけて(오키오 츠케테)\n \
                <프랑스어> - Au revoir(오 뷔 부아)\n \
                <중국어> -再见。(짜이찌엔)\n \
                <스페인어> - ¡Adiós!(아디오스)"]
    #교무실에서의 번역

    sc_go_2lang = ["[문 좀 닫아줘] \n \
    <영어> - Please close the door. (플리즈 클로우즈 더 도어)\n \
    <일본어> - ドアを閉めてくれ(도아오 시메테쿠레) \n \
    <중국어> - 把门关上 (바뭉궝샤)\n \
    <스페인어> - Cierra la puerta.(시롸 라  푸에레타) \n \
    <프랑스어> -Fermez la porte. (셔우미 레 포우트) ",
        "[이것 좀 주워주라]  \n 영어 : Pick this up, please.(픽 디스 업 플리즈) \n \
        일본어: これちょっと拾ってやれ (코레 초토 힛토테야레) \n \
        중국어: 把这个捡起来(빠 쳐 끄어 칭췰라우 ) \n \
        프랑스어: s'il te plaît. (실 토 플렡) \n \
        스페인어: Dame esto. (다메 예시토)",
        "[다음과목이 뭐야?]  \n 영어 : What's the next subject? (왓츠 더 넥스트 서브직트) \n \
        일본어: 次の科目は何? (츠키노 카모쿠와 나니) \n \
        중국어: 下一个科目是什么? (샤이 크어크어 무 슈어 샹마) \n \
        프랑스어:Quelle est la prochaine matière ? (케릴라 푸슈엉 마츠하) \n \
        스페인어: ¿Cuál es el siguiente curso? (꽐리 셸리 슈기엔트 구숴)",
        "[조용히 좀 해주라]  \n 영어 : Please be quiet. (플리즈 비 콰이엍) \n \
        일본어: 静かにしてくれ(시즈카니 시테쿠레) \n \
        중국어: 安静点 (안 증 디언) \n \
        프랑스어:Tais-toi. (데 투아) \n \
        스페인어: Cállate. (까이야테)"]
    #교실에서의 번역
    def run(self,User_S):
        #실행하고서 처음 딱 선택하는 글들 
    
            # for start
       #제일 큰 테마를 고름

        school = School._tema[int(User_S)-1]    #학교에서,회사에서 등등등을 골랐을때 

        for i in school:                    #반복문 사용해서 하나씩 뽑기 (교무실, 교실)이 출력
            print(i,"\t",end="")
        print()
        User = input("한번더 선택해 주세요")    #교무실, 교실중 선택하기
        if int(User) == 1:
            User_g = input(School._tema_go[int(User)-1])         #교무실 했을 때 표현들이 출력됨   
            print(School._sc_go_1lang[int(User_g)-1])     #교무실의 표현1들을 출력하는 것.
        elif int(User) == 2:
            User_g2 = input(School._tema_go[int(User)-1])       
            print(School.sc_go_2lang[int(User_g2)-1])     

        print()