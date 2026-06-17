# Harness Week 1: Git, Docker, YAML

这个小项目用来完成第一周的入门练习。

目标：

1. 用 Git 记录代码变化。
2. 读懂最基本的 YAML。
3. 用 Docker 把一个小服务打包成镜像。
4. 用 Docker Compose 启动服务。
5. 跑起 Harness，并理解 Harness Pipeline 和本项目的关系。

## 项目结构

```text
hello-harness/
  app.py                # 一个很小的 HTTP 服务
  Dockerfile            # 告诉 Docker 如何构建镜像
  compose.yaml          # 告诉 Docker Compose 如何启动服务
  config.example.yaml   # YAML 语法练习
  .harness/pipeline.yaml # Harness 会读取的 CI pipeline
  harness-pipeline.yaml  # 额外的 pipeline 示例
  test_app.py            # 最小单元测试
```

## 今天先记住三个概念

Git 是代码历史记录器：它记录“谁在什么时候改了什么”。

Docker 是环境打包器：它把程序和运行环境一起装进镜像，别人可以用同样方式运行。

YAML 是配置文件格式：它用缩进表达层级，经常用于 CI/CD、Docker Compose、Kubernetes 等工具。

## 常用命令

```bash
git status
git add .
git commit -m "first week practice"
docker build -t hello-harness:week1 .
docker run --rm -p 19080:8080 hello-harness:week1
docker compose up --build
docker compose down
```

## Harness 和这个项目的关系

Harness Pipeline 可以自动执行你手工敲的命令，例如：

```bash
python -m py_compile app.py test_app.py
python -m unittest -v
```

也就是说，先理解本地命令，再理解 pipeline，会轻松很多。
