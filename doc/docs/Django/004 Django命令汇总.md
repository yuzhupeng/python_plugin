# Djang 命令汇总

## 创建Django工程
```bash
django-admin startproject project_name
```

## 创建子应用app
```bash
python manage.py startapp app_name
```

## 运行项目
```bash
python manage.py runserver
```

## 生成迁移脚本
```bash
python manage.py makemigrations project_name
```
## 查看创建表sql语句
```bash
python manage.py sqlmigrate project_name 迁移脚本
```

## 执行迁移脚本
```bash
python manage.py migrate project_name
python manage.py migrate
```

## 根据现有数据库建立model
```bash
python manage.py inspectdb
```

## 把模型文件导入到app中
```bash
python manage.py startapp app
python manage.py inspectdb > app/models.py
```