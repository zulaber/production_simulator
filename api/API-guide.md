
# REST API documentation
>  All endpoints explained

## Login

Use API as admin:

login: admin

password: admin

Token: 9f48c04891191596323c448ae24af79824b4b4c4

or as user -> [users_informations.txt](../Assets/users_informations.txt)

Random token from User -> Token: 7d6a5ca494efb8b2de99b1019d8dc2ffeeec2a82

*there is diffrent permisions for user or staff

## Endpoints

| URI                                              | GET                                                 | POST                                  | PUT                               | DELETE                                      |
| ----------------------------------------------------- | --------------------------------------------------- | ------------------------------------- | --------------------------------- | ------------------------------------------- |
| [/api/v1/](#URIs)                             | Returns set of URIs | N/A                                   | N/A                               | N/A                                         |
| [/api/get-token](#Token)                                 | N/A                            | Returns token for user                 | N/A                               | N/A                                         |
| [/api/v1/users/](#Users)                                 | Returns a list of users                           | N/A                   | N/A                               | N/A                                         |
| [/api/v1/users/{id}](#Users)                                 | Returns a user                           | N/A                   | N/A                               | N/A                                         |
| [/api/v1/informations/](#Informations)                                 | Returns a list of informations                           | Creates a new information                   | N/A                               | N/A                                         |
| [/api/v1/informations/{id}](#Informations)                                 | Returns a information                           |   N/A                 | Updates a information                               | Deletes a information                                        |N/A 
| [/api/v1/tools/](#Tools)                                 | Returns a list of tools                           | Creates a new tool                   | N/A                               | N/A                                         |
| [/api/v1/tools/{id}](#Tools)                                 | Returns a tool                           |   N/A                 | Updates a tool                               | Deletes a tool                                        |N/A 
| [/api/v1/tools/{id}/detail/](#Tools)                                 | Returns a more detailed data of tool                           |     N/A                | N/A                               | N/A                                         |
| [/api/v1/projects/](#Projects)                                 | Returns a list of projects                           | Creates a new project                   | N/A                               | N/A                                         |
| [/api/v1/projects/{id}](#Projects)                                 | Returns a project                           |   N/A                 | Updates a project                               | Deletes a project                                        |N/A 
| [/api/v1/projects/{id}/detail/](#Projects)                                 | Returns a more detailed data of project                           |     N/A                | N/A                               | N/A                                         |
| [/api/v1/employees/](#Employees)                                 | Returns a list of employees                           | Creates a new employee                   | N/A                               | N/A                                         |
| [/api/v1/employees/{uuid}](#Employees)                                 | Returns a employee                           |   N/A                 | Updates a employee                               | Deletes a employee                                        |N/A 
| [/api/v1/employees/{uuid}/detail/](#Employees)                                 | Returns a more detailed data of employee                           |     N/A                | N/A                               | N/A                                         |
| [/api/v1/producers/](#Producers)                                 | Returns a list of producers                           | Creates a new producer                   | N/A                               | N/A                                         |
| [/api/v1/producers/{id}](#Producers)                                 | Returns a producer                           |   N/A                 | Updates a producer                               | Deletes a producer                                        |N/A 
| [/api/v1/producers/{id}/detail/](#Producers)                                 | Returns a more detailed data of producer                           |     N/A                | N/A                               | N/A                                         |

### URIs

#### Single example: 

```
{
    "users": "https://productionsimulator.herokuapp.com/api/v1/users/",
    "informations": "https://productionsimulator.herokuapp.com/api/v1/informations/",
    "tools": "https://productionsimulator.herokuapp.com/api/v1/tools/",
    "projects": "https://productionsimulator.herokuapp.com/api/v1/projects/",
    "employees": "https://productionsimulator.herokuapp.com/api/v1/employees/",
    "producers": "https://productionsimulator.herokuapp.com/api/v1/producers/"
}
```

| URI | Method   |**GET** |
| --- |  ------- |  ------- |
| `/api/v1/`  | Permission |All      |

> GET

Returns set of avalible URIs.

### Token

#### Single example: 

```
{
    "token": "dee9a966e4fe39abf1e59b9e950d28632e4454f6"
}
```

#### Permissible Fields

| Element / Attribute     | POST       |  
| ----------------------- | --------- | 
| **username**                    | Required  | 
| **password**              | Required   |

| URI | Method   |**POST** |
| --- |  ------- |  ------- |
| `/api/get-token`  | Permission |All      |

> POST

Returns token for user.

### Users

#### Single example: 

```
{
    "id": 3,
    "username": "qobuckpzsua",
    "first_name": "Jakub",
    "last_name": "Chmielewska",
    "email": "tyxwhl@mail2joey.com",
    "branch": "Lublin",
    "image": "https://production-simulator-live.s3.eu-west-2.amazonaws.com/profile_image/7.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVGRKEV6O54SLRAVI%2F20200609%2Feu-west-2%2Fs3%2Faws4_request&X-Amz-Date=20200609T123809Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=90c2e8237f94dcdcc7aaa064ac8f8f118681770c00511f824af65e33dae485c5"
}
```

#### Sortable Fields

| Filter                | Type | lookups           | Description |
| --------------------- | --|---------------- | ----------- |
| **search**                | String| SearchFilter           | Search given value in: username, last_name, email, branch  |
| **fields**      | String|Selective fields          | Returns only selected fields |
| **omit**      | String|Selective fields          | Returns all fields except omitted ones |
| **page**      |Integer |Pagination          | Returns page |
| **page_size**      | Integer|Pagination          | Returns number of records on page (default=50, max_page_size=500 |

| URI                  | Method         |**GET**     |
| -------------------- |  ------------- |  --------- |
| `/api/v1/users/`  | Permission     | Users      | 

> GET

Returns list of users with branch and image.

| URI | Method   |**GET** |
| --- |  ------- |  ------- |
| `/api/v1/users/{id}`  | Permission |Users      |

> GET

Returns informations about user with branch and image.

### Informations

#### Single example: 

```
{
    "id": 1009,
    "author": 2,
    "title": "fdsfsf3ds2",
    "info": "fdsfsfs",
    "date_posted": "2020-05-16"
}
```

#### Permissible Fields

| Element / Attribute     | PUT       | POST      |
| ----------------------- | --------- | --------- |
| **id**                  | Forbidden | Forbidden |
| **author**              | Forbidden | Forbidden |
| **title**               | Required  | Required  |
| **info**                | Required  | Required  |
| **date_posted**         | Forbidden | Forbidden |

#### Sortable Fields

| Filter                | Type | lookups           | Description |
| --------------------- | --|---------------- | ----------- |
| **id**                |Integer    |exact, in         | Django’s built-in lookup |
| **author**                | Integer   |exact, in           | Django’s built-in lookup |
| **title**                |  String  |exact, icontains           | Django’s built-in lookup |
| **info**                |   String |exact, icontains            | Django’s built-in lookup |
| **date_posted**                |Date    |exact, icontains, gt, gte, lt, lte, year, month, day, range           | Django’s built-in lookup |
| **my**                |Boolean    |   custom      | If my=True, returns all informations created by current user |
| **ordering**                | String   |     order_by    | Can order by: author, id, date_posted  |
| **search**                | String| SearchFilter           | Search given value in: title, info  |
| **fields**      | String|Selective fields          | Returns only selected fields |
| **omit**      |String |Selective fields          | Returns all fields except omitted ones |
| **page**      | Integer|Pagination          | Returns page |
| **page_size**      | Integer|Pagination          | Returns number of records on page (default=100, max_page_size=1000 |

| URI                  | Method         |**GET**     |**POST** |
| -------------------- |  ------------- |  --------- |-------- |
| `/api/v1/informations/`  | Permission     | All      | Users   |

> GET

Returns list of Informations

> POST

Adds new Information 

| URI                  | Method         |**GET** |**PUT**     |**DELETE** |
| -------------------- |  ------------- |--------- |  --------- |-------- |
| `/api/v1/informations/{id}`  | Permission     |All      | Users(creator)      | Users(creator)   |

> GET

Return single Information

> PUT

Updates Information

> DELETE

Deletes Information

### Tools

#### Single example: 

```
{
    "tool_id": 1309,
    "geometry": "Ball",
    "material": "HSS",
    "diameter_mm": "14.80",
    "shank_diameter_mm": "15.0",
    "tool_radius_mm": "7.40",
    "tool_length_mm": "70.00",
    "working_part_length_mm": "50.0",
    "compensation_mm": 0.47,
    "producer": 3,
    "status": "Utilize the tool",
    "price": "47.50",
    "date_of_purchase": "2019-08-22",
    "project": 63
}
```

#### Permissible Fields

| Element / Attribute     | PUT       | POST      |
| ----------------------- | --------- | --------- |
| **id**                    | Forbidden  | Forbidden |
| **geometry**              | Required   | Required  |
| **material**          | Required   | Required  |
| **diameter_mm**             | Required   | Required  |
| **shank_diameter_mm**              | Allowed   | Allowed  |
| **tool_radius_mm**              | Allowed   | Allowed  |
| **compensation_mm**              | Allowed   | Allowed  |
| **tool_length_mm**              | Allowed   | Allowed  |
| **working_part_length_mm**              | Allowed   | Allowed  |
| **producer**              | Allowed   | Allowed  |
| **status**              | Allowed   | Allowed  |
| **price**              | Required   | Required  |
| **producer**              | Allowed   | Allowed  |
| **date_of_purchase**              | Forbidden   | Forbidden  |

#### Sortable Fields

| Filter                | Type | lookups           | Description |
| --------------------- | --|---------------- | ----------- |
| **tool_id**                | Integer   |    exact, in    |Django’s built-in lookup  |
| **geometry**                | String   |    exact, icontains    |Django’s built-in lookup  |
| **material**                | String   |    exact, icontains    |Django’s built-in lookup  |
| **diameter_mm**                | Float    |    exact, icontains, gt, gte, lt, lte, range    |Django’s built-in lookup  |
| **shank_diameter_mm**                | Float    |    exact, icontains, gt, gte, lt, lte, range      |Django’s built-in lookup  |
| **tool_radius_mm**                | Float   |    exact, icontains, gt, gte, lt, lte, range    |Django’s built-in lookup  |
| **tool_length_mm**                | Float   |    exact, icontains, gt, gte, lt, lte, range    |Django’s built-in lookup  |
| **working_part_length_mm**                | Float   |    exact, icontains, gt, gte, lt, lte, range    |Django’s built-in lookup  |
| **compensation_mm**                | Float   |    exact, icontains, gt, gte, lt, lte, range    |Django’s built-in lookup  |
| **producer**                | Integer   |    exact, in    |Django’s built-in lookup  |
| **status**                | String   |    exact, icontains    |Django’s built-in lookup  |
| **price**                | Float   |    exact, icontains, gt, gte, lt, lte, range     |Django’s built-in lookup  |
| **date_of_purchase**                | Date   |    exact, icontains, gt, gte, lt, lte, year, month, day, range     |Django’s built-in lookup |
| **project**                | Integer   |    exact, in    |Django’s built-in lookup  |
| **ordering**                |  String  |     order_by    | Can order by: tool_id, diameter_mm, shank_diameter_mm, tool_radius_mm, tool_length_mm, working_part_length_mm, compensation_mm, price, date_of_purchase  |
| **fields**      | String|Selective fields          | Returns only selected fields |
| **omit**      |String |Selective fields          | Returns all fields except omitted ones |
| **page**      | Integer|Pagination          | Returns page |
| **page_size**      | Integer|Pagination          | Returns number of records on page (default=200, max_page_size=2000 |
 

| URI                  | Method         |**GET**     |**POST** |
| -------------------- |  ------------- |  --------- |-------- |
| `[/api/v1/tools/`  | Permission     | Users      | Users   |

> GET

Returns list of Tools

> POST

Adds new Tool 

| URI                  | Method         |**GET** |**PUT**     |**DELETE** |
| -------------------- |  ------------- |--------- |  --------- |-------- |
| `/api/v1/tools/{id}`  | Permission     |Users      | Users      | Users   |

> GET

Return single Tool

> PUT

Updates Tool

> DELETE

Deletes Tool

| URI                  | Method         |**GET**     |
| -------------------- |  ------------- |  --------- |
| `/api/v1/tools/{id}/detail/`  | Permission     | Users      |

> GET

Returns single Tool with extra data about project and producer

### Projects

#### Single example: 

```
{
    "project_id": 43,
    "project_name": "Soax ",
    "time_for_project_hours": "135.00",
    "profit": "47029.00",
    "employees": [
        "fd4a8baf-b10a-453c-8cc9-c5da58629a03",
        "287ca1af-8db9-48af-b1ef-225fb7082dde",
        ...
        "c8dcdc49-ddcc-46fa-829a-d6769ff9e2ce",
        "de281243-c1e0-47d9-a55d-dfbb0d4f7b7d"
    ],
    "tools": [
        974,
        1100
    ]
}
```

#### Permissible Fields

| Element / Attribute     | PUT       | POST      |
| ----------------------- | --------- | --------- |
| **project_id**                    | Forbidden  | Forbidden |
| **project_name**              | Required   | Required  |
| **time_for_project_hours**          | Required   | Allowed  |
| **profit**             | Required   | Required  |
| **employees**              | Allowed   | Allowed  |
| **tools_id**              | Forbidden   | Allowed  |


#### Sortable Fields

| Filter                | Type | lookups           | Description |
| --------------------- | --|---------------- | ----------- |
| **project_id**                | Integer   |    exact, in    |Django’s built-in lookup  |
| **project_name**                | String   |    exact, icontains    |Django’s built-in lookup  |
| **time_for_project_hours**                | Float   |    exact, icontains, gt, gte, lt, lte, range    |Django’s built-in lookup  |
| **profit**                | Float    |    exact, icontains, gt, gte, lt, lte, range    |Django’s built-in lookup  |
| **employees**                | UUID    |    exact    |Django’s built-in lookup  |
| **ordering**                |  String  |     order_by    | Can order by: project_id, time_for_project_hours, profit  |
| **fields**      | String|Selective fields          | Returns only selected fields |
| **omit**      |String |Selective fields          | Returns all fields except omitted ones |
| **page**      | Integer|Pagination          | Returns page |
| **page_size**      | Integer|Pagination          | Returns number of records on page (default=10, max_page_size=50 |

| URI                  | Method         |**GET**     |**POST** |
| -------------------- |  ------------- |  --------- |-------- |
| `/api/v1/projects/`  | Permission     | Users      | Users   |

> GET

Returns list of Projects

> POST

Adds new Project 

| URI                  | Method         |**GET** |**PUT**     |**DELETE** |
| -------------------- |  ------------- |--------- |  --------- |-------- |
| `/api/v1/projects/{id}`  | Permission     |Users      | Users      | Users   |

> GET

Return single Project

> PUT

Updates Project

> DELETE

Deletes Project

| URI                  | Method         |**GET**     |
| -------------------- |  ------------- |  --------- |
| `/api/v1/projects/{id}/detail/`  | Permission     | Users      |

> GET

Returns single Project with extra data about tools and employees

### Employees

#### Single example: 

```
{
    "uuid_employee": "0b2807ac-1129-4a3d-bc7f-0e0771ee8652",
    "first_name": "Maxymilian",
    "last_name": "Adamczyk",
    "email": "eamjabytyohxrsp@ivillage.com",
    "phone_number": "+48664818336",
    "date_of_employment": "2001-04-07",
    "position": {
        "position_id": 1,
        "position_name": "Junior - operator",
        "hourly_rate": 20.0
}
```

#### Permissible Fields

| Element / Attribute     | PUT       | POST      |
| ----------------------- | --------- | --------- |
| **uuid_employee**                    | Forbidden  | Forbidden |
| **first_name**              | Required   | Required  |
| **last_name**          | Required   | Required  |
| **email**             | Allowed   | Allowed  |
| **phone_number**              | Allowed   | Allowed  |
| **date_of_employment**              | Forbidden   | Forbidden  |
| **position**              | Allowed   | Allowed  |

#### Sortable Fields

| Filter                | Type | lookups           | Description |
| --------------------- | --|---------------- | ----------- |
| **employees**                | UUID   |    exact    |Django’s built-in lookup  |
| **first_name**                | String   |    exact, icontains    |Django’s built-in lookup  |
| **last_name**                | String   |   exact, icontains    |Django’s built-in lookup  |
| **email**                | String    |    exact, icontains     |Django’s built-in lookup  |
| **phone_number**                | String    |    exact, icontains   |Django’s built-in lookup  |
| **date_of_employment**                | Date    |    exact, icontains, gt, gte, lt, lte, year, month, day, range    |Django’s built-in lookup  |
| **position**                | Integer    |    exact, in     |Django’s built-in lookup  |
| **ordering**                |   String |     order_by    | Can order by: date_of_employment, position  |
| **fields**      | String|Selective fields          | Returns only selected fields |
| **omit**      |String |Selective fields          | Returns all fields except omitted ones |
| **page**      | Integer|Pagination          | Returns page |
| **page_size**      | Integer|Pagination          | Returns number of records on page (default=100, max_page_size=1000 |

| URI                  | Method         |**GET**     |**POST** |
| -------------------- |  ------------- |  --------- |-------- |
| `/api/v1/employees/`  | Permission     | Users      | Users   |

> GET

Returns list of Employee

> POST

Adds new Employee 

| URI                  | Method         |**GET** |**PUT**     |**DELETE** |
| -------------------- |  ------------- |--------- |  --------- |-------- |
| `/api/v1/employees/{uuid}`  | Permission     |Users      | Users      | Users   |

> GET

Return single Employee

> PUT

Updates Employee

> DELETE

Deletes Employee

| URI                  | Method         |**GET**     |
| -------------------- |  ------------- |  --------- |
| `/api/v1/employees/{uuid}/detail/`  | Permission     | Users      |

> GET

Returns single Employee with extra data about projects that he/she is in






### Producers

#### Single example: 

```
{
    "producer_id": 5,
    "producer_name": "Ceratizit",
    "contact_person": "Petra Zalewska",
    "phone_number": "+48567557587",
    "email": "cywfesjxzal@ttml.co.in",
    "rabat": "23.10",
    "delivery_time_days": "4-9"
}
```

#### Permissible Fields

| Element / Attribute     | PUT       | POST      |
| ----------------------- | --------- | --------- |
| **producer_id**                    | Forbidden  | Forbidden |
| **producer_name**              | Required   | Required  |
| **contact_person**          | Required   | Required  |
| **phone_number**             | Allowed   | Allowed  |
| **email**              | Allowed   | Allowed  |
| **rabat**              | Required   | Required  |
| **delivery_time_days**              | Allowed   | Allowed  |

#### Sortable Fields

| Filter                | Type | lookups           | Description |
| --------------------- | --|---------------- | ----------- |
| **search**                |String | SearchFilter           | Search given value in: producer_name, contact_person, email, phone_number  |
| **ordering**                |  String  |     order_by    | Can order by: dproducer_id, rabat  |
| **fields**      | String|Selective fields          | Returns only selected fields |
| **omit**      |String |Selective fields          | Returns all fields except omitted ones |
| **page**      | Integer|Pagination          | Returns page |
| **page_size**      | Integer|Pagination          | Returns number of records on page (default=10, max_page_size=50 |

| URI                  | Method         |**GET**     |**POST** |
| -------------------- |  ------------- |  --------- |-------- |
| `/api/v1/producers/`  | Permission     | Users      | Users   |

> GET

Returns list of Producers

> POST

Adds new Producer 

| URI                  | Method         |**GET** |**PUT**     |**DELETE** |
| -------------------- |  ------------- |--------- |  --------- |-------- |
| `/api/v1/producers/{id}`  | Permission     |Users      | Users      | Users   |

> GET

Return single Producer

> PUT

Updates Producer

> DELETE

Deletes Producer

| URI                  | Method         |**GET**     |
| -------------------- |  ------------- |  --------- |
| `/api/v1/producers/{id}/detail/`  | Permission     | Users      |

> GET

Returns single Producer with list of tools provided by him/her
