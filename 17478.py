N = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

def printBar(N):
    for n in range(N):
        print("____",end="")

def recursiveFunction(count):
    printBar(count)
    print("\"재귀함수가 뭔가요?\"")
    if count == N:
        printBar(count)
        print("\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    else:
        printBar(count)
        print("\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        printBar(count)
        print("마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        printBar(count)
        print("그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        recursiveFunction(count + 1)

    printBar(count)
    print("라고 답변하였지.")
    return

recursiveFunction(0)