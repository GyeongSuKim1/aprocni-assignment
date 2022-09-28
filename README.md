# aprocni-assignment
- 기간 22.09.21 ~ 22.9.28

## Mission
- 등록 항목 정의
  - 기본항목 : 글쓴이, 비밀번호(암호화 필요), 제목, 내용, 등록자 IP
  - 추가적인 정보는 개발에 필요에 따라 추가 하십시요

- 댓글, 좋아요 기능을 가지고 있어야 함
  - 좋아요는 사용자 IP를 기준으로 게시글당 1회만 좋아요를 할 수 있다
  - 댓글은 부적절한 단어를 포함 하는 경우 등록을 차단 (서버에서 차단 처리)
    - (부적절 단어 : 일상에서 나쁘게 쓰이는 욕을 몇개 정하여 사용하십시요)
    
- 게시글 테이블은 2개로 생성하여 등록순서 홀짝으로 구분하여 등록한다.
  - 게시글 테이블 board_A, board_B 이름으로하며 board_A 게시글 홀수 번호, board_B 게시글 짝수번호 등록이 되도록 하십시요

- 리스트, 조회, 삭제, 수정 기능을 구현 하십시요

- 테이블 생성 스크립트 첨부 바랍니다.

> IP구현을 못하였습니다.

## Project
### 사용 스텍
- python
- Django rest framework

## ERD
![image](https://user-images.githubusercontent.com/89643366/192090330-366269ad-e0b3-4654-92ab-ce23172383d6.png)

## API명세서
![image](https://user-images.githubusercontent.com/89643366/192774792-ec5b9200-c204-48b2-89bd-f7b16bfd3e80.png)

## 테이블 생성 스크립트
![image](https://user-images.githubusercontent.com/89643366/192777346-c2b79324-d88b-4f57-8363-44a0fb977715.png)
