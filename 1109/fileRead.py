from pathlib import Path

FILE = Path(__file__).resolve()  # __file__은 현재 파일에 대한 path
print(FILE)
ROOT = FILE.parent # 파일을 소유하고 있는 부모

if __name__ == '__main__':
    f = open(ROOT / 'hello.txt', 'r+', encoding='UTF-8') # w를 쓰면 읽을 수 없어서 오류나고, 파일 내용은 다 지워지게 된다.
    #읽기
    #print(f.readlines())
    #print(f.readline())
    #print(f.read())

    #쓸수있는지 여부
    #print(f.writable())

    #쓰기
    #f.write("Write new line, please")
    #f.writelines(["\nWirte new line, please", "\nsecond new line"])

    #커서위치
    print(f.tell())
    savePoint = f.seek(0,2)
    f.write("\nWrite is inportant!!")
    f.seek(savePoint)
    print(f.read())


    f.close()