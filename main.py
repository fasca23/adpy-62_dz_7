class Stack:
    
    def __init__(self):
       self.stack = []
    
    # проверка стека на пустоту. Метод возвращает True или False
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    # разбиваем строчку на символы и добавляем в стек    
    def push_element_str(self, item_str):
        for i in item_str:
            self.stack.append(i)
    
    # добавляет новый элемент на вершину стека. Метод ничего не возвращает   
    def push(self, item):
         self.stack.append(item)

    # удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        return self.stack.pop()
    
    # возвращает верхний элемент стека, но не удаляет его. Стек не меняется
    def peek(self):
        return self.stack[len(self.stack)-1]
    
    # возвращает количество элементов в стеке
    def size(self):
        return len(self.stack)
    
    # возвращает весь стек
    def show_stack(self):
            return(self.stack)

a = input("Введите строку содержащую стек: ")
s=Stack()
flVerify = True
for i in a:
    if i in "([{":
        s.push(i)
        # print(s.show_stack())
    elif i in ")]}":
        if s.size() == 0:
            flVerify = False
            break
        br = s.pop()
        if br == '(' and i == ')':
            continue
        if br == '[' and i == ']':
            continue
        if br == '{' and i == '}':
            continue
        flVerify = False
        break

if flVerify and s.size() == 0:    
    print("Сбалансированно")
else:
    print("Несбалансированно")