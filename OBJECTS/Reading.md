## 내가 알았던 객체지향 이란
- 객체 간의 상호작용을 통해 작동하는 프로그램을 만드는 Paradigm
- 잘 만들어진 객체지향이란 → 객체간의 책임이 뚜렷하고, 경계가 명확하며, 일관성 있는 의존성을 가져야한다.

#### 성질
- Abstraction : 객체에서 행위(Method)와 속성(Property)를 추출하는 것
- Encapsulation : 객체에 변수와 함수를 묶는 것
- Inheritance : 부모 객체의 속성을 자식에게 물려 주는 것
- Polymorphism : 같은 이름이지만 다른 행동을 하는 것 → Overriding / Overloading

#### Q/A
Q. Overriding / Overloading 시에 Return 값은 어떻게 되어야하는가?  
A. Overriding 시에는 무조건 같아야 하고, Overloading 시에는 다를 수도 있다. Calculator의 Add(int, int) -> int 를 생각해보면 쉽게 이해할 수 있을 듯

#### 잘 설계하기 위해서는 → SOILD
- Single Responsibility : 객체는 단 한가지일만 수행하여야 한다
- Open-Closed : 인터페이스 등을 사용하여 기존의 코드를 변경하지 않으면서 추가할 수 있도록 하여야 한다.
- Liskov Substituition : 자식은 부모가 하는 행동을 수행할 수 있어야 한다.
- Interface Segregation : 인터페이스는 작고 구체적이야 한다.
- Dependency Inversion : 객체간의 의존관계는 원칙을 가지고 있어야 한다.
