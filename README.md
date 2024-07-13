**다음의 지시문을 바탕으로 만들어진 과제 레포지토리 입니다.**

1. **밥먹어U를 구현해봅시다.**

 밥먹어U의 가장 기본은 식단표를 저장했다 불러오는 기능이에요. 아래 endpoint로 들어오는 요청을 처리하는 Backend를 구현해봅시다.

- **POST /api/set/bap**
    
    식당 이름과 메뉴가 들어왔을 때, 해당 값을 저장하는 기능을 수행합니다.
    
    ```jsx
    request
    {
    	rest_name : str
    	menus : List[str]
    }
    ```
    
- **GET /api/get/bap/<rest_name>**
    
    식당 이름이 들어왔을 때, 저장해놓은 메뉴를 반환합니다.
    
    ```jsx
    respond
    {
    	menus : List[str]
    }
    ```
    

단, 조건이 있어요. 아래 글을 보고 VS Code에서 Python의 Type을 검사해주는 기능을 활성화해주세요. 그리고 코드엔 빨간줄이 없어야해요. 타입의 설정 방법은… 검색을 통해 알아봅시다.
