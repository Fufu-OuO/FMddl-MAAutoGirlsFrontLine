<!-- markdownlint-disable MD033 MD041 -->
<div align="center">
  <img alt="LOGO" src="./assets/images/logo/FMddl-logo_1280×1280.png" width="256" height="256" />
<br>
<img alt="Name" src="./assets/images/Name.png" width="270" height="33" />

# GirlsFrontLine

**费马**<sup>FM</sup>**大定理**<sup>Deadline</sup>，基于 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 所提供模板，是少女前线**国服桌面端**的自动化助手。

# 脚本存在封号风险，请勿以任何形式跳脸官方，<br>使用费马即默认自担风险；<br><br>本项目完全开源，如果你花钱购买了费马，
<img alt="YOUARETREATED" src="./assets/images/youaretreated.gif" width="284" height="43" />

</div>

## 功能

- **后勤**：自动收取后勤，~~允许重置后勤对齐进度。~~
- **日常**：消耗动能、势能，完成每日事务，领取协议及活跃度奖励。
- **刷本**：~~仅支持部分副本拖尸、打捞（如8-1N等）~~，视情况适配活动打捞。
- **托管**：定时启动，托管设置项目。

## 修改费马与游戏设置

**烦请对照表格，自行修改费马与游戏的设置，以免出现大量报错。**

> ### 费马 => 左下角设置

#### => 左侧边栏：运行设置

| 运行设置                            | 值   |
| ----------------------------------- | ---- |
| 任务运行失败后是否继续运行其它任务    | 是 |

#### => 左侧边栏：连接设置

| 连接设置                            | 值   |
| ----------------------------------- | ---- |
| 捕获方式                             | 无边框窗口：GDI 或 FramePool</p>　窗口化　：GDI |
| 触控方式                             |  Seize  |

> ### 游戏主界面 => 右下角切换栏目 => 设置

#### => 左侧边栏：基础

| 图像设置                            | 值   |
| ----------------------------------- | ---- |
| 分辨率                               | 16:9（≥720p） |
| 显示模式                             | 无边框窗口（必须屏幕原生16:9，不能在16:10屏幕上 ```alt``` + ```enter``` 拉伸！）</p>　窗口化 |
| 高帧数模式                           | 开 |
| 兵棋画面模式                         | 帧率优先 |

| 功能设置                            | 值   |
| ----------------------------------- | ---- |
| 剧情播放                            | 单次 |
| 锁定新角色                          | 开 |
| 图鉴评价                            | 关 |
| 台词字幕                            | 关 |
| 自动播放速度                        | 最大 |

#### => 左侧边栏：作战

| 战场设置                            | 值   |
| ----------------------------------- | ---- |
| 自动补给                            | 关 |
| 战场信息                            | 关 |
| 自动释放妖精技能                     | 开 |
| 是否打开记录上次完成关卡时镜头缩放    | 关 |
| 代理作战使用机动装甲                 | 开 |

| 战斗设置                            | 值   |
| ----------------------------------- | ---- |
| 调整阵型效果                        | 冻结时间 |
| 选中人形效果                        | 冻结时间 |
| 人形梯队技能演出                    | 关闭 |
| 融合势力技能演出                    | 关闭 |
| 重创保护                            | 开 |
| 战斗简化                            | 开 |
| 伤害数字简化                        | 开 |

## 常见问题

> **为什么费马不能帮我打开游戏？**<p>
MAAFramework下的win32状态，总是先捕获到一个窗口再开始运行，费马无法在没有打开游戏的情况下捕获游戏窗口╮(╯▽╰)╭</p>
> **为什么脚本会抢鼠标？**<p>
国服目前只有桌面端，运行脚本时游戏窗口必须保持在前台，所以本项目这点上不像Alas、MAA等项目，而是更像BetterGI、三月七，必然抢鼠标(ó﹏ò｡)</p>
> **为什么找不到自动后勤的功能？如何设置我的后勤？**<p>
后勤完成界面会于游戏停留在主页面时自动弹出，如果不及时点掉必然报错，故费马自带了**不可取消**的后勤重复功能。<p>
~~⚠️以下为“后勤重复”功能：除了启动定时费马的用户可以在**第一次运行**时，借助该功能对齐时间以外，该功能无需选中⚠️<p>
如果确定需要启动该功能，请参考下图：~~</p>

## 鸣谢

本项目由 **[MaaFramework](https://github.com/MaaXYZ/MaaFramework)** 强力驱动！  
UI 由 [MFAAvalonia](https://github.com/SweetSmellFox/MFAAvalonia)大力支持！

## 感谢 **[MAAGF1](https://github.com/LeonNagant/MaaGF1_Test)** 开发组对本项目的支持与贡献！