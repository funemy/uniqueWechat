#### Unique Studio报名微信后台

----------------------------------------------------------------------

**报名接口：**

	/wechat

	POST

	数据库的账户密码修改handler.py中的`USERNAME`和`PASSWD`

**表单格式：**

- `name`:[Unicode, nullable=False]


- `gender`:[Unicode, nullable=False]


- `campus`:[Unicode, nullable=False]

	单选框

	数据格式:yy/zs/qy

- `major`:[Unicode, nullable=False]


- `contact`:[BigInteger, nullable=False]


- `backup_contact`:[BigInterger, **nullable=True**]


- `group`:[Unicode, nullable=False]

	单选框

	数据格式:Android/Web/iOS/Design/lab/PM

- `intro`:[Unicode, **nullable=True**]
  
  ​