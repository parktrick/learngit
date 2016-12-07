## 运行django,到mysite_django目录下运行:
```python
python3 manage.py runserver 127.0.0.1:9000
```

## 访问地址:
    - 登录地址: 127.0.0.1:9000/login/
    - 注册地址: 127.0.0.1:9000/register/
    - DATA地址: 127.0.0.1:9000/data/1/


## 测试用户:
    - UserName: admin
    - Password: 123456


## javascript
    - /statics/js/juqery-1.12.4.js
    - /statics/js/table_from.js    # DATA页面表达操作
    - /statics/js/table_verify.js  # 注册页面表单验证


----
### 说明
> 这是一个基于之前得前端技术在django上实现的一个web服务,测试学习~

> 1. 登录界面做了简单用户密码验证.
> 2. 注册页面做前端js表单验证.
> 3. 数据展示页面实现了全选,取消,反选等批量操作;
> 4. 点击进入编辑模式按钮,将使得所有的选择操作(点击勾选按钮,和批量选举按钮)都会让选中得那一行进入到一个编辑得状态;
> 5. 添加按钮会在表格顶部添加一行新的表格,并进入编辑状态.
> 6. 在所有的编辑状态中按回车都会确认保存数据,后端服务器进行更新,刷新页面!
> 7. 删除按钮会删除删除当前选中的所有数据,并在后端服务器进行更新!