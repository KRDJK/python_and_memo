#파일을 만들 때는 mkdir이 아니라 touch!
#ex) touch apple grape orange
# 그냥 파일을 만들기 위해 이렇게 하는 것이고 뒤에 확장자로 메모장, 한글파일 등등 만들기
# 마스터 폴더에서 하위 폴더로 갔을 때, 연동된 가장 큰 폴더!(rot 폴더)에서 add하기.
# git add .
# 커밋할 때, -m을 뒤에 붙이지 않으면 연동된 텍스트 프로그램이 등장하고, 거기서를 통해 좀 더 많은 설명을 붙일 수 있음.


# git + tag + 내가 붙이고 싶은 넘버링 붙이기 + 넘버링 하려는 커밋 식별번호 입력!!
# git + tag + 넘버링까지 해놓고 + -m "first version ~~" 설정 가능.
# git + diff 해놓고 + 파일명(+항상 확장자까지)까지 입력하면 그 해당 파일의 변경점만을 보여줌.
# git log --stat이라고 치면 디테일하게 나오고 스크롤은 방향키 위아래로 움직일 수 있음 나올 때는 q 키를 눌러 나옴.
# git log -p 라고 하면 --stat보다 훨씬 더 자세하게 각각의 커밋에서 디테일하게 어떤 부분이 바뀌었는지까지 나옴. 파일의 내용 등 / 역시나 나올 때는 q를 눌러 나옴.


# git checkout + 내가 보고자 하는 이전 커밋의 식별번호
# 체크아웃으로 가기 전에 작업 중이던게 있으면 안됨. 커밋하고 가라고 안내문 나옴.
# 체크아웃으로 이동한 후, 거기서 또 깃 로그를 확인해보면 해당 체크아웃한 곳 까지만 로그가 나옴.
# 체크아웃 시점에서의 파일들이 다 복구가 되고, 해당 체크아웃 시점보다 미래 시점은 없어짐.
# git log --oneline --all로 하면 체크아웃까지만의 시점이 아닌 숨어있는 모든 로그가 나옴.
# 체크아웃을 했다고 완전히 그 시점으로 돌아간게 아니라 그냥 과거 시점을 한 번 들여다본 것.
# 체크아웃으로 돌아가서 새로운 시도를 해보고 만약 그게 별로면 다시 돌아갈 수 있는 기능.
# git checkout master로 입력하면 로컬의 가장 최근의 커밋으로 회귀함.
# 로컬의 최신 버전이 아닌, 깃허브의 최신 상태로 가고 싶다면 git checkout origin master

## reset과 checkout의 차이점 ##
# 원격에 8번까지 했는데 로컬에서 11번까지 진행함. 근데 11, 10번이 아예 잘못된 경우!
# 9번으로 리셋으로 가버리면 해결!
# git reset --hard 9번의 커밋 식별번호
# 원래 checkout을 하면 헤드만 이동하고 master는 최근 로컬로 유지였는데 reset을 하면 헤드랑 마스터가 같이 이동.
# 해당 reset 칸이 제일 최근 로컬이 되어버림.

## soft reset이란?
# 9번으로 soft reset을 하면 아예 지워버리진 않고 9번 이후의 파일들을 워킹 트리에 남겨둠.
# 그래서 add만 된 채로, 커밋 되기 전 상태가 되기 때문에 조금은 더 안전한 리셋이 가능.
#매우 중요 # soft 커밋으로 5번을 돌아가면 가장 최근 로컬(9번이라고 예시)까지의 만들어졌던 파일, 앱 등이 사라지는 것이 아님.
## 그래서 그 상태로 add .을 하고 새로 6번으로 커밋을 한다면 5번에서 나머지 9번까지의 파일들을 합친 새로운 6번을 탄생시키는 것이 가능.


### 하드 리셋을 했는데 엥?? 괜히 지웠네? ###
# 복구가 가능한 경우!!! 해당 하드 리셋으로 지운 커밋 식별번호를 알고 있는 경우에는 복구가 가능함. 다시 git reset --hard 지웠던 커밋의 식별번호
## 하드 리셋으로 지우기 전에 캡쳐본을 떠둔다거나 식별번호를 저장할 수 있음!!
# 따로 백업하기 전에 캡처본 같은걸 떠두지 않고 clear 명령어로 화면까지 날렸다면 복구 불가능.

### 이미 깃허브에 올라간 파일들 이전으로 reset을 할 때는?? ###
# 할 수는 있지만.. 그 전의 기록(이력)들은 남아있음


## branch ##
# a가 혼자서 버전 3개를 만듦
# 이 3개의 branch를 마스터 브랜치라고 함. v1, v2, v3
# v4부터 b가 개발에 참여하기 시작함.
# a와 b가 각자의 로컬에서 v4를 제작함. 그럼 같은 v4가 아님.
# 원격에 둘 다 푸시를 하면 문제가 생김.
# 인원수가 많을 경우 협의를 해가며 누구거를 올릴지 결정하기가 쉽지 않음.

# #2
# a는 v4를 개발하고, 동시에 그 시간에 b는 v5를 개발함.
# 곁가지(branch)를 파서 메인스트림에 영향이 가지 않게 하면서 작업함.
# branch를 하면 잘못됐을 때 메인 스트림이 아닌 곁가지 치기를 하면 됨.
## 팀장이 메인스트림을 관리하고 팀원의 곁가지들을 팀장이 검토하는 것이 가능함. 괜찮으면 합류(머지 merge)시키고 이상하면 자르는 것이 가능.##

## 예제 ##
# 둘리 - 팀 소개(team.txt), 자기소개 작성(doolri.txt)
# 도우너 - 팀소개(team.txt), 자기소개 작성(dounat.txt)
## 이 경우, 팀 소개는 충돌이 일어남(둘의 파일명이 같기 때문), 각자의 자기소개서는 충돌 없음.
# 각자의 브랜치를 만들어줌. git branch doolri, git branch dounat
# 이 경우, git branch라고만 치면 브랜치 목록들이 보임. 그럼 메인의 master까지 3개의 브랜치가 생성된 것을 확인 가능.
# 이러고 git log --oneline --all 을 치면 헤드 -> 마스터, 둘리, 도우너라고 나옴
# 둘리의 입장에서는 저 헤드를 둘리로 옮겨야함. git checkout doolri 라고 하면 헤드가 둘리로 이동됨.

# git log --oneline --all --graph -> 헤드 마스터를 기준으로 갈래를 뻗어나간 곁가지들이 보임.

### 둘리의 브랜치를 마스터에 합쳐줄(nerge) 땐???
# git merge doolri 이렇게 하고 로그 기록 확인하면 합쳐진게 눈에 보임. 헤드가 옮겨짐.
# git merge dounat을 하면 충돌이 일어남. team.txt가 같기 때문.
# 그렇게 하면 team.txt가 하나만 보이지만 그걸 열어보면 둘리와 도우너가 쓴게 하나에 합쳐진거처럼 보임.
# 거기서 팀장이 수동으로 어느 것을 쓸지 선택할 수 있음.
# 협업아닌 혼자 할 때도 이 방법을 사용할 수 있음. 안전하게.
# merge를 써서 합쳤어도 그 이전으로 reset을 통해 돌아가는 것도 가능함.
# 역할이 끝난 브랜치는 정리해줌 git branch -d doolri dounat

#### merge도 push만큼 신중하게 해야함!!!! ####