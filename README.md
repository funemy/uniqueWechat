## Unique Studio报名微信后台

#### **报名接口**

	/applicant

	POST

	数据库的账户密码修改database.py中的`USERNAME`和`PASSWD`

	数据库地址修改database.py中的`URL`

**表单格式：**

- `name`:[Unicode, nullable=False]


- `gender`:[Unicode, nullable=False]


- `campus`:[Unicode, nullable=False]

	单选框

	数据格式:yy/zs/qy

- `major`:[Unicode, nullable=False]


- `contact`:[BigInteger, nullable=False]


- `backup_contact`:[BigInterger, **nullable=True**]
  
  当**该项为空**时
  
  POST数据请**不要有backup_contact这个条目**


- `group`:[Unicode, nullable=False]

	单选框

	数据格式:Android/Web/iOS/Design/lab/PM

- `intro`:[Unicode, **nullable=True**]

#### 联系接口

	/advice

	POST

	数据库的账户密码修改handler.py中的`USERNAME`和`PASSWD`

	数据库地址修改handler.py中的`URL`

**表单格式：**

- `name`:[Unicode, nullable=False]
- `major`:[Unicode, nullable=False]
- `email`:[Unicode, nullable=False]
- `advice`:[Unicode, nullable=False]



#### 部署说明：

运行环境：`python3`

依赖包：`wtforms` `sqlalchemy` `tornado`

数据库：`mysql` 数据库的账号密码在database.py里改