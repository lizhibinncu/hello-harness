# 第一周学习清单

## Day 1: 跑通本地练习项目

重点：

- `git status` 查看当前变化。
- `docker build` 构建镜像。
- `docker compose up` 启动服务。
- 浏览器打开 `http://localhost:19080`。

练习：

```bash
git log --oneline
docker images | grep hello-harness
docker compose ps
curl http://localhost:19080
```

## Day 2: Git 基础

重点：

- 工作区：你正在编辑的文件。
- 暂存区：`git add` 放进去的文件。
- 提交历史：`git commit` 保存下来的版本。

练习：

```bash
git status
git diff
git add README.md
git commit -m "update notes"
git log --oneline
```

## Day 3: YAML 基础

重点：

- 缩进表达层级。
- `key: value` 表达配置项。
- `- item` 表达列表。
- `|-` 表达多行脚本。

练习文件：

```text
config.example.yaml
.harness/pipeline.yaml
harness-pipeline.yaml
compose.yaml
```

## Day 4: Dockerfile

重点：

- `FROM` 选择基础镜像。
- `WORKDIR` 设置工作目录。
- `COPY` 复制文件。
- `EXPOSE` 声明容器端口。
- `CMD` 设置启动命令。

练习：

```bash
docker build -t hello-harness:day4 .
docker run --rm -p 19081:8080 hello-harness:day4
```

## Day 5: Docker Compose

重点：

- Compose 用 YAML 描述多个服务。
- `ports` 的左边是宿主机端口，右边是容器端口。
- `docker compose down` 用来停止并清理本项目容器。

练习：

```bash
docker compose up -d --build
docker compose logs
docker compose down
```

## Day 6: Harness 初体验

访问：

```text
http://localhost:3300
```

练习：

- 注册第一个用户。
- 创建第一个 Space 或 Project。
- 创建或导入一个 Repository。
- 找到 Pipeline 入口，但先不要追求复杂配置。

## Day 7: 串起来

你应该能解释：

- Git 负责记录代码历史。
- YAML 负责描述配置。
- Docker 负责统一运行环境。
- Harness Pipeline 负责自动执行构建、测试、发布命令。

复盘命令：

```bash
git log --oneline
docker ps
docker images
docker compose ps
```
