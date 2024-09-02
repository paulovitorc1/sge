# SGE - Inventory Managemnt System

### Definition of Functional and Non-Functional Requirements

##### Functional Requirements
- Registration of products, brands, suppliers, categories, stock entries, and exits
- Product filtering
- Automatic calculation of available stock quantity for each product, based on recorded entries and exits
- User login system
- User and/or group permission control, including different access levels
- Dashboards with metrics and charts for sales, stock entries, exits, and stock value
- Support for future integrations/automations

##### Non-Functional Requirements
- Security
- Performance
- Scalability
- Usability
- Maintainability
- Responsiveness



### MER - Entity-Relationship Diagram

![image](https://github.com/user-attachments/assets/8b83a834-8997-467a-9155-a6d2846bcd71)

### Tech Stack and Architecture

**Django**
- Admin panel for managing users and permissions
- User structure, sessions, login, permissions, and groups
- Already in use by the team (familiar stack)
- Can be full stack with Bootstrap (sufficient for current needs)

**Bootstrap**
- Integrated with Django for front-end needs

**Chart.js**
- Selected for dashboard requirements (easy to use)

**Django REST Framework**
- API within the same project to support future integrations/automations and the possibility of a decoupled frontend

