# Git 安装与配置指南（Windows）

## 一、Git 安装步骤

### 1. 运行安装程序
- 找到你下载的 Git 安装文件（通常命名为 `Git-2.x.x-64-bit.exe`）
- 双击运行安装程序
- 出现用户账户控制提示时，点击「是」

### 2. 关键选项选择

#### 2.1 选择安装目录
- 可以使用默认目录（推荐）：`C:\Program Files\Git`
- 或者选择你喜欢的其他目录
- 点击「Next」

#### 2.2 选择组件
- **必选组件**：保持默认选择即可
- **可选组件**（推荐勾选）：
  - `Git LFS (Large File Support)`：支持大文件版本控制
  - `Git Bash Here`：在右键菜单中添加 Git Bash 选项
  - `Git GUI Here`：在右键菜单中添加 Git GUI 选项
  - `Add a Git Bash Profile to Windows Terminal`：添加到 Windows Terminal
- 点击「Next」

#### 2.3 选择开始菜单文件夹
- 使用默认名称「Git」即可
- 点击「Next」

#### 2.4 选择默认编辑器
- 推荐选择你熟悉的编辑器：
  - 初学者推荐：`Notepad++`（需要先安装）或 `Visual Studio Code`
  - 高级用户：`Vim`（默认选项，但学习曲线较陡）
- 点击「Next」

#### 2.5 调整新仓库的默认分支名称
- 推荐使用 `main`（GitHub 等平台的默认分支名）
- 点击「Next」

#### 2.6 选择 Git 环境变量
- 推荐选择：`Git from the command line and also from 3rd-party software`
- 这个选项会将 Git 添加到系统 PATH 中，方便在命令行和其他软件中使用
- 点击「Next」

#### 2.7 选择 HTTPS 传输后端
- 使用默认选项：`Use the OpenSSL library`
- 点击「Next」

#### 2.8 选择行结束符处理
- 推荐选择：`Checkout Windows-style, commit Unix-style line endings`
- 这个选项能很好地兼容 Windows 和 Linux/macOS 系统
- 点击「Next」

#### 2.9 选择 Git Bash 终端模拟器
- 使用默认选项：`Use MinTTY (the default terminal of MSYS2)`
- 这个终端功能更强大
- 点击「Next」

#### 2.10 选择 Git Pull 行为
- 使用默认选项：`Default (fast-forward or merge)`
- 点击「Next」

#### 2.11 选择 Git Credential Manager
- 推荐选择：`Git Credential Manager Core`
- 这个选项能帮助你管理 Git 凭证（用户名/密码或令牌）
- 点击「Next」

#### 2.12 选择额外选项
- 可以勾选：`Enable file system caching` 和 `Enable symbolic links`
- 点击「Next」

#### 2.13 开始安装
- 点击「Install」按钮开始安装
- 等待安装完成（通常需要 1-2 分钟）
- 点击「Finish」完成安装

## 二、安装完成后验证

1. 打开命令提示符（Win+R → 输入 `cmd` → 回车）或 Git Bash
2. 输入以下命令查看 Git 版本：
   ```bash
   git --version
   ```
3. 如果显示版本信息（如 `git version 2.45.1.windows.1`），说明安装成功

---

## 三、Git 基本配置（必做）

### 1. 配置用户名和邮箱

这是最基本也是最重要的配置，Git 使用这些信息来标识你的提交。

#### 1.1 打开命令行工具
- 可以使用 `Git Bash`（安装时选择了就会在右键菜单中）
- 或者使用 `Windows 命令提示符`（Win+R → 输入 `cmd` → 回车）
- 或者使用 `Windows Terminal`

#### 1.2 设置全局用户名
运行以下命令（替换为你的用户名）：
```bash
git config --global user.name "你的用户名"
```

例如：
```bash
git config --global user.name "kaneshiro"
```

#### 1.3 设置全局邮箱
运行以下命令（替换为你在 GitHub/GitLab 等平台使用的邮箱）：
```bash
git config --global user.email "你的邮箱@example.com"
```

例如：
```bash
git config --global user.email "kaneshiro@example.com"
```

#### 1.4 验证配置
运行以下命令查看是否配置成功：
```bash
git config --global --list
```

你应该能看到类似这样的输出：
```
user.name=kaneshiro
user.email=kaneshiro@example.com
```

## 四、Git 其他重要配置

### 1. 配置默认编辑器

如果你在安装时没有选择合适的编辑器，可以通过命令行重新配置：

```bash
# 使用 Visual Studio Code（推荐）
git config --global core.editor "code --wait"

# 使用 Notepad++
git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"

# 使用 Vim（默认）
git config --global core.editor "vim"
```

### 2. 配置行结束符

行结束符是一个重要的配置，特别是当你在不同操作系统间协作时：

```bash
# Windows 推荐设置
git config --global core.autocrlf true

# macOS/Linux 推荐设置
git config --global core.autocrlf input

# 禁用自动转换（不推荐）
git config --global core.autocrlf false
```

### 3. 启用颜色显示

让 Git 输出更加美观易读：

```bash
git config --global color.ui true
```

### 4. 配置命令别名

为常用命令设置快捷键，提高工作效率：

```bash
# 查看状态的快捷方式
git config --global alias.st status

# 查看日志的快捷方式
git config --global alias.logg "log --oneline --graph --decorate --all"

# 查看差异的快捷方式
git config --global alias.d diff

# 提交的快捷方式
git config --global alias.c commit

# 分支的快捷方式
git config --global alias.br branch

# 切换分支的快捷方式
git config --global alias.co checkout
```

使用示例：
```bash
git st  # 相当于 git status
git logg  # 相当于 git log --oneline --graph --decorate --all
git d  # 相当于 git diff
```

### 5. 配置 Pull 行为

设置 Git 默认的拉取行为：

```bash
# 默认（快进或合并）
git config --global pull.rebase false

# 总是变基（推荐，保持提交历史线性）
git config --global pull.rebase true
```

### 6. 配置缓存凭证

让 Git 记住你的用户名和密码/令牌，避免每次都输入：

```bash
# 使用 Git Credential Manager Core（推荐，安装时已默认配置）
git config --global credential.helper manager-core
```

## 五、验证 Git 安装和配置成功

### 1. 验证 Git 安装

运行以下命令检查 Git 是否安装成功：

```bash
git --version
```

如果安装成功，你会看到类似这样的输出：
```
git version 2.45.1.windows.1
```

### 2. 验证全局配置

运行以下命令查看所有全局配置：

```bash
git config --global --list
```

你应该能看到你设置的所有配置，例如：
```
user.name=kaneshiro
user.email=kaneshiro@example.com
core.editor=code --wait
core.autocrlf=true
color.ui=true
alias.st=status
alias.logg=log --oneline --graph --decorate --all
alias.d=diff
alias.c=commit
alias.br=branch
alias.co=checkout
```

### 3. 测试基本 Git 操作

让我们创建一个测试仓库来验证 Git 是否能正常工作：

#### 3.1 创建一个测试目录

```bash
# 创建目录
mkdir test-git

# 进入目录
cd test-git
```

#### 3.2 初始化 Git 仓库

```bash
git init
```

你会看到类似这样的输出：
```
Initialized empty Git repository in C:/Users/kaneshiro/test-git/.git/
```

#### 3.3 创建一个测试文件

```bash
# 创建文件
echo "Hello Git!" > hello.txt

# 查看文件内容
cat hello.txt
```

#### 3.4 添加文件到暂存区

```bash
git add hello.txt
```

#### 3.5 提交文件

```bash
git commit -m "Add hello.txt"
```

你会看到类似这样的输出：
```
[master (root-commit) 1a2b3c4] Add hello.txt
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt
```

#### 3.6 查看提交历史

```bash
git log
```

或者使用我们配置的别名：
```bash
git logg
```

你会看到你的提交记录。

#### 3.7 清理测试目录

```bash
# 返回上一级目录
cd ..

# 删除测试目录（可选）
rmdir /s test-git
```

## 六、配置 SSH 密钥用于 GitHub 认证（推荐）

### 1. SSH 密钥的作用

使用 SSH 密钥可以：
- 无需每次推送/拉取代码都输入密码
- 提供更高的安全性
- 方便与 GitHub/GitLab 等平台进行认证

### 2. 检查是否已有 SSH 密钥

首先检查是否已经存在 SSH 密钥：

```bash
# 列出 SSH 密钥文件
ls -la ~/.ssh
```

如果已经有 SSH 密钥，你会看到类似这样的文件：
- `id_rsa`（私钥，不要分享给任何人）
- `id_rsa.pub`（公钥，可以分享）

### 3. 生成新的 SSH 密钥

如果没有 SSH 密钥或者想生成新的，可以运行以下命令：

```bash
ssh-keygen -t rsa -b 4096 -C "你的邮箱@example.com"
```

例如：
```bash
ssh-keygen -t rsa -b 4096 -C "kaneshiro@example.com"
```

运行命令后，你会看到类似这样的提示：

```
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/kaneshiro/.ssh/id_rsa):
```

按回车使用默认位置即可。

接下来会提示你输入密码（可选，但推荐）：

```
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

输入密码后，你会看到类似这样的输出：

```
Your identification has been saved in /c/Users/kaneshiro/.ssh/id_rsa.
Your public key has been saved in /c/Users/kaneshiro/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx kaneshiro@example.com
The key's randomart image is:
+---[RSA 4096]----+
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
|                 |
+----[SHA256]-----+
```

### 4. 将 SSH 密钥添加到 ssh-agent

#### 4.1 启动 ssh-agent

```bash
eval $(ssh-agent -s)
```

你会看到类似这样的输出：
```
Agent pid 1234
```

#### 4.2 添加私钥到 ssh-agent

```bash
ssh-add ~/.ssh/id_rsa
```

如果设置了密码，会提示你输入密码。

### 5. 将 SSH 公钥添加到 GitHub 账户

#### 5.1 复制公钥内容

```bash
# 方法一：使用 cat 命令查看并手动复制
cat ~/.ssh/id_rsa.pub

# 方法二：直接复制到剪贴板（Windows）
clip < ~/.ssh/id_rsa.pub

# 方法三：直接复制到剪贴板（macOS）
pbcopy < ~/.ssh/id_rsa.pub
```

公钥内容看起来像这样：
```
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC1234567890...+更多字符... kaneshiro@example.com
```

#### 5.2 添加到 GitHub

1. 登录 GitHub
2. 点击右上角头像 → 选择「Settings」
3. 在左侧菜单选择「SSH and GPG keys」
4. 点击「New SSH key」
5. 输入「Title」（例如：「My Laptop」）
6. 在「Key」字段粘贴刚才复制的公钥内容
7. 点击「Add SSH key」
8. 可能需要输入 GitHub 密码进行确认

### 6. 测试 SSH 连接

运行以下命令测试是否能成功连接到 GitHub：

```bash
ssh -T git@github.com
```

如果是第一次连接，会看到类似这样的提示：

```
The authenticity of host 'github.com (140.82.121.4)' can't be established.
RSA key fingerprint is SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

输入 `yes` 并按回车。

如果连接成功，你会看到类似这样的输出：

```
Hi kaneshiro! You've successfully authenticated, but GitHub does not provide shell access.
```

### 7. 使用 SSH URL 克隆仓库

现在你可以使用 SSH URL 而不是 HTTPS URL 来克隆仓库了：

```bash
# SSH URL 格式
git clone git@github.com:用户名/仓库名.git

# 例如
git clone git@github.com:kaneshiro/kaneshiron.git
```

## 七、总结

恭喜你！现在你已经成功安装并配置了 Git。你可以开始使用 Git 进行版本控制了。

### 常用 Git 命令

- `git init`：初始化 Git 仓库
- `git clone [URL]`：克隆远程仓库
- `git add [文件]`：添加文件到暂存区
- `git commit -m "提交信息"`：提交文件
- `git push`：推送到远程仓库
- `git pull`：从远程仓库拉取
- `git status`：查看状态
- `git log`：查看提交历史
- `git branch`：查看分支
- `git checkout [分支]`：切换分支
- `git merge [分支]`：合并分支

### 进一步学习

- [Git 官方文档](https://git-scm.com/doc)
- [GitHub Git 指南](https://guides.github.com/introduction/git-handbook/)
- [Git 教程 - 廖雪峰](https://www.liaoxuefeng.com/wiki/896043488029600)

祝你使用 Git 愉快！