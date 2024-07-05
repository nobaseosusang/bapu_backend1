**다음의 지시문을 바탕으로 만들어진 과제 레포지토리 입니다.**

**1주차**

**밥먹어U를 구현해봅시다.**

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

**2주차**

1. **디자인 패턴**

  프로젝트가 커질수록 코드를 짜는 규칙이 중요해요. 이런 규칙을 쓰는 이유가 몇가지 있어요.

1. 협업에 중요함.
2. 효율적임.
3. https://ittrue.tistory.com/550
4. …

Backend에선 MVC 디자인 패턴을 사용할거에요. Backend(특히 Python)은 이와 관련된 자료가 많아 추가적인 설명이 없어도 될거같아요. 혹시 검색하실때, flask mvc boilerplate와 같이 boilerplate를 검색하면 좋은 예를 많이 찾을 수 있어요. 우선 이전에 작성한 코드를 MVC 패턴으로 리펙토링 해주세요. 리펙토링 시 프로젝트의 폴더 구조를 어떻게 해야할지 생각하며 짜면 좋아요.

1. **기능 변경**

 앞에 디자인 패턴과 이어져요. 저번시간엔 하나의 식당에 대한 식단 정보만 개별적으로 저장했어요. 이번엔 API를 조금 수정할 거에요.

- **POST /api/set/bap**
    
    식당 이름과 메뉴가 들어왔을 때, 해당 값을 저장하는 기능을 수행합니다.
    
    ```python
    request
    {
    	date : Datetime
    	meal_type : Literal["BREAKFAST", "LAUNCH", "DINNER"]
    	rest_name : str
    	menus : List[str]
    }
    ```
    
- **GET /api/get/bap/<start_time>/<end_time>**
    
    해당 시점에 있는 식당의 식단 정보를 모두 가져와요.

  response
{
	results : List[Meal]
}


Meal
{
	date : Datetime
	meal_type : Literal["BREAKFAST", "LAUNCH", "DINNER"]
	rest_name : str
	menus : List[str]
}
