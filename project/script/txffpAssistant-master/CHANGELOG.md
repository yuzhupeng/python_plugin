## <small>1.1.0 (2020-9-24)</small>

* perf: 优化睡眠，使用范围随机值取代固定值 cc80b6a
* refactor: 更改HTTP请求头信息 74abb89
* feat: 新增开票功能 c69cf9e



## <small>1.0.4 (2020-09-21)</small>

* feat: 新增请求睡眠间隔时间设置参数 dd6fdd6
* perf: 优化会话 05cd77b



## <small>1.0.3 (2020-08-07)</small>

* fix: 修正setup版权信息错误 dea45e6
* feat: debug模式下，打印详细错误信息 1414bd8
* feat: 使用更加优美的表格显示数据信息 a51ab7d
* feat: 增加下载完成后，输出表格数据 0e4ad2c
* feat: 添加对Ctrl+C按键的异常捕捉 d2744a9
* docs: 修正文档错误 3a3aaa9



## <small>1.0.2 (2020-08-01)</small>

* feat: 加入问题反馈说明 bda083d
* feat: 添加微信扫码捐赠 c2edec6
* 更新版本信息至1.0.2 f0cd458
* fix: 修复--merge参数错误 c4f55d2



## <small>1.0.1 (2020-08-01)</small>

* feat: 加入pdf文件合并成功提示 a8a36d4
* feat: 支持命令行参数调用 b8bb666
* feat: 更新版本信息至1.0.1 26f7b06
* feat: 打包处理 20369bc
* feat: 新增get_zipfile函数 652db8c
* feat: 增加异常捕捉 67ab1eb
* feat: 新增发票下载 97990e3
* feat: 新增选项--simple 0aff534
* feat: 加入安装验证和脚本命令 1cd628f
* refactor: 更改导入方式 67dfbc7
* refactor: 更改文件合并参数默认为False e288eca
* refactor: 更改语法，以支持python3.4 4081695
* refactor: 更改部分日志信息的等级 350ca46
* refactor: 重构验证和命令执行 2a512be
* fix: 修复inv_id信息错误 3f079eb
* fix: 优化class_name的生成 e4ff938
* fix: 修复月份为01到09报错的bug 555c959
* fix: 修正获取开票时间 90a9253
