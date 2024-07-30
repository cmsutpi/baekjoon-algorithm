#노드의 수는 처음 입력받은수
node = int(input().strip())
#트리의 형태로 딕셔너리 선택
tree = {}
#처음 주어진 노드의 수 크기만큼 입력을 받아 bt딕셔너리에 키는 root로 값은 각 left와 right로 추가
for count in range(node):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

# 입력받은 트리를 각각 전위 중위 후위 순회 했을 때를 print하는 함수 작성
# print할때 아래로 쭉 나오지 않고 옆으로 이어서 하기위해 end 추가

def preorder(root): # 전위순회
    if root != '.':
        print(root, end = '')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root): # 중위순회
    if root != '.':
        inorder(tree[root][0])
        print(root, end = '')
        inorder(tree[root][1])

def postorder(root): # 후위순회
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')