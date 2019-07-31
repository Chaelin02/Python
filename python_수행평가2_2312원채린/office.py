# from public import Public
class Office:
    _tema = [["1.교무실에서","2.교실에서"],  #학교에서
        [None,None,None],  #회사에서
        ["패스트푸드점에서","쇼핑할때","대중교통을 이용할때"],          #공공장소
        [None,None,None]]                                                        #일상생활에서

    _tema_Of = ["1.결제 부탁드립니다.\
                2.외근 다녀오겠습니다.\
                3.식사는 어떻게 할까요?\
                4. 사인 부탁드립니다."]


    _sc_of_1lang = ["[결제 부탁드립니다.] \n <영어> - Please pay for it.(플리즈 페이 포어 잇) \n \
    <일본어> - 決済をお願いします。(켓사이오 오네가이시마스)\n \
    <프랑스어> - Je vous prie de payer. (즈 부 프위 더 풰이에)\n \
    <중국어> -请结算。(징 지일 쑤와이))\n \
    <스페인어> - Por favor, dame el pago. (포르 파보르 다메 에르 파고))",
        "[외근 다녀오겠습니다.] \n<영어> -I'll be back from work. (아일 비 백 프럼 웍)\n \
        <일본어> - 外勤に行ってきます。 (가이킨니 잇테키마스)\n \
        <프랑스어> -Je vais travailler à l'extérieur. (즈 비 탈레기 알레스타일리어)\n \
        <중국어> -我去外勤了。(워 취 와 칑 러)\n \
        <스페인어> - Voy a trabajar afuera.(보이 아 뜨뤠브아 카할라 푸에라)",
        "[식사는 어떻게 할까요?] \n <영어> -How do you like your meal? (하우 두 유 라익 요어 밀)\n \
            <일본어> -食事はどうしましょうか。 (쇼쿠지와 도오시마쇼오카)\n \
            <프랑스어> - Que voulez-vous manger ? (쿠 블뤼브 모우쉬?)\n \
            중국어> - 吃饭要怎么做? (쉬 퐈 야우 쫘마 쯔우어)\n \
            <스페인어> - ¿Qué tal la comida?(쿠 탈라 코미다)",
            "[사인 부탁드립니다.]\n <영어> - Please sign your name. (플리즈 사인 유아 네임)\n \
                <일본어> - 署名してください。 (쇼메에시테쿠다사이)\n \
                <프랑스어> - Veuillez signer, s'il vous plaît.(브이엥 증에 시 부 플레)\n \
                <중국어> -请签字。(칭치엥 쓰) \n \
                <스페인어> -Firme, por favor. (프이르메, 포르 파보르)"]

    def run(self,User_S):

            # for start
        #User_S = input("알고싶은 표현을 선택하세요")    #제일 큰 테마를 고름

        office = Office._tema[int(User_S)-1]    #학교에서,회사에서 등등등을 골랐을때 사용자가 누른번호에서 -1을 해줌. 

        for i in Office._tema_Of:                    #반복문 사용해서 하나씩 뽑기 회사에서의 문장들. (4개)
            print(i,"\t",end="")
        print()

        User = input("한번더 선택해 주세요")    #4개의 문장에서 선택하기.

        print(Office._sc_of_1lang[int(User)-1])     #4개의 문장에서 출력하기.

        print()