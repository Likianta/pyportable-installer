# 3.x

## 3.2.1

* 新增: `项目模板:module_paths` 支持 `{dist_root}` 和 `{dist_lib}` 插值
* 新增: 解决 tkinter 的打包问题
* 新增: 解决 pywin32 的打包问题

## 3.2.0 | 2021-05-26

* 变更: 调整 venv 的创建方式

## 3.1.1

* 变更: `assets_copy.copy_assets` 在复制时包含隐藏文件夹
* 修复: `项目模板:module_paths` 恢复使用
* 修复: 恢复 `aftermath` 模块

## 3.0.0

* 变更: 基于 pyarmor 混淆代码, 取代编译为 pyc 文件
* 变更: 重构程序处理流程
* 变更: 重新设计 IO 流程

--------------------------------------------------------------------------------

# 2.x

## 2.3.0 | 2021-04-21

* 变更: 基于 PyArmor 编译源文件
* 变更: 逐步切换到 rst 格式的文档
* 变更: prebuild.py 重命名为 main.py
* 新增: bootloader.txt 支持目标模块无调用函数的情况

## 2.2.3

编译优化

* 优化: `compile_dir` 的编译结果直接放在与 py 同目录下

## 2.2.2

* 优化: 使用 vbscript 弹窗替代 tkinter 弹窗
* 移除: 对 tkinter 的依赖
* 移除: 从 prebuild 中移除中文路径的检查
* 优化: launch_by_system.bat 模板
* 修复: `prebuild._copy_assets` 拷贝时的范围选取过大
* 优化: 调整 prebuild.min_build 的行为

## 2.2.1

* 新增: 定位 embed_python 资源

all-in-one 配置文件 (pyproject.json)

* 修复: `shutils.copytree` 拷贝 venv 时报 "目录已存在" 错误
* 变更: 重构 pyproject.json 的结构
* 新增: `pyproject.json:build:enable_console` 选项
* 新增: pyportable-installer 通过自举的方式完成项目打包

## 2.2.0 | 2021-03-07

* 变更: 项目重命名: "lkdist" -> "pyportable-installer"

## 2.1.2

* 新增: 图片 (jpg, png, etc.) 转 ico 模块
* 新增: 当打包路径中含有中文字符时给予提示

## 2.1.1

* 更新: 从 bootloader.txt 中移除海象运算符, 使支持 Python 3.7 及以下的版本
* 修复: bootloader.txt 模板中相对路径计算可能出现错误
* 修复: bootloader.txt `os.chdir` 参数错误
* 新增: 在 `prebuild.py:_precheck_args` 中检查读我文档的路径

## 2.1.0 | 2021-03-06

* 新增: bat 转 exe 工具
* 优化: 将 bat 转 exe 操作放在子线程中运行

## 2.0.0 | 2021-03-06

* 重新设计 pyproject.json 的结构
* 重构 prebuild.py

--------------------------------------------------------------------------------

# 1.0

## 1.0.0 | 2021-01-00

* 新增: 为 enable_venv 提供 embed python
* 新增: 包含 tkinter 模块的 embed python
* 新增: full_build 和 min_build