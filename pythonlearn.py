<<<<<<< HEAD
print("Hello Python")
=======
# < SQL 툴 제작 >

# create 파일명 : 파일 제작
# insert 파일명 내용 : 파일에 내용 추가
# select 파일명 : 파일 읽기
# update 파일명 기존내용 대체내용: 파일의 기존내용을 대체내용으로 바꿈
# delete 파일명 : 파일 삭제 

from glob import glob
import os

def create(fname) :
    check = glob("*.txt")
    checkNum = 0
    for i in check :
        i = i[:len(i) - 4]
        if i == fname :
            print("< 이미 같은 이름의 파일이 있습니다 >")
            checkNum = 1
    if checkNum == 0 :
        fp = open(fname + ".txt", 'w')
        print(fname + " 이라는 이름의 파일을 생성했습니다.")

def insert(fname) :
    check = glob("*.txt")
    checkNum = 0
    for i in check :
        i = i[:len(i) - 4]
        if i == fname :
            checkNum = 1
    if checkNum == 0:
        print("< 파일이 없습니다 >")
    else :
        text = input("추가할 내용을 입력해 주세요 >> ")
        fp = open(fname + '.txt', 'a')
        fp.write(text)
        fp.write("\n")
        print(fname  +" 파일에 " + text + " 내용이 추가되었습니다.")

def select(fname) :
    check = glob("*.txt")
    checkNum = 0
    for i in check :
        i = i[:len(i) - 4]
        if i == fname :
            checkNum = 1
    if checkNum == 0 :
        print("< 해당 파일이 없습니다 >")
    else :
        fp = open(fname + ".txt", 'r')
        print("< 파일 내용 >")
        print(fp.read())

def update(fname) :
    check = glob("*.txt")
    checkNum = 0
    for i in check:
        i = i[:len(i) - 4]
        if i == fname :
            checkNum = 1
    if checkNum == 0 :
        print("< 해당 파일이 없습니다 >")
    else :
        fp = open(fname + ".txt", 'r')
        text = fp.read()
        fp.close()
        search = input("바꿀 글을 입력하세요 >> ")
        if search in text :
            new = input("대체할 글을 입력하세요 >> ")
            text = text.replace(search, new)
            print(text)
            fp = open(fname + ".txt", 'w')
            fp.write(text)
            fp.close()
            print("< 글이 대체 되엇습니다 >")
        else :
            print("< 해당 글이 없습니다 >")
        


def delete(fname) :
    check = glob("*.txt")
    checkNum = 0
    for i in check :
        i = i[:len(i) - 4]
        if i == fname:
            checkNum = 1
    if checkNum == 0:
        print("< 해당 파일이 없습니다 >")
    else :
        os.remove(fname + ".txt")
        print("< 해당 파일이 삭제 되었습니다 >")

def checkCommand(command) :
    if command == "create" :
        print("< 파일 생성 명령 입력 받음 >")
        fname = input("파일 이름을 입력해 주세요 >> ")
        create(fname)
    elif command == "insert" :
        print("입력 명령 입력 받음")
        fname = input("파일 이름을 입력해 주세요 >> ")
        insert(fname)
    elif command == "select" :
        print("파일 읽기 명령 입력 받음")
        fname = input("읽을 파일 이름을 입력해 주세요 >> ")
        select(fname)
    elif command == "update" :
        print("파일 내용 업데이트 명령 입력 받음")
        fname = input("파일 이름을 입력해 주세요 >> ")
        update(fname)
    elif command == "delete" :
        print("파일 삭제 명령 입력 받음")
        fname = input("삭제할 파일 이름을 입력해 주세요 >> ")
        delete(fname)
    else :
        print("오류")

print(" < SQL 프로그램 >")
while True :
    command = input("명령을 입력해주세요 >> ")
    if command == "exit" :
        print("< SQL을 종료합니다 >")
        break
    else:
        checkCommand(command)

>>>>>>> 44305e82e7a42426d900161ba581716ea12b2c12
