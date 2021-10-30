https://ofcourse.kr/

10/2
vscode에서 github에 파일을 올리려는데 파일이 비어있다고 오류가 떳다.
-> laboratory에 있던 css와 js파일에 아무것도 적혀있지 않았기 때문. 둘을 삭제하고 업로드 하니 잘 되었다.

10/21
hordes.io

10/23
https://rogerdudler.github.io/git-guide/index.ko.html
github 설명 사이트
https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/
github 토큰 설명
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
토큰 설정 설명

fatal: Unable to create '/home/runner/Programming/.git/index.lock': File exists.

Another git process seems to be running in this repository, e.g.
an editor opened by 'git commit'. Please make sure all processes
are terminated then try again. If it still fails, a git process
may have crashed in this repository earlier:
remove the file manually to continue.
깃 사용 중 프로세스 충돌
index.lock 파일을 삭제하면 됨.
cd로 이동 후 rm으로 삭제

push가 안 될 때 강제실행
git push -f origin main 