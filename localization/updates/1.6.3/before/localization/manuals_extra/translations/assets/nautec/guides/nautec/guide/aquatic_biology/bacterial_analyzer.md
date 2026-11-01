---
navigation:
  title: 细菌分析机
  icon: nautec:bacterial_analyzer
  position: 4
  parent: aquatic_biology/aquatic_biology-index.md
item_ids:
  - nautec:bacterial_analyzer
  - nautec:advanced_bacterial_analyzer
---

# <Color id="light_purple">细菌分析机</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="bacterial_analyzer" scale="2"/>
  细菌分析机可显示菌落的规模, 活力和属性.
</Column>

将装有未分析菌落的<ItemLink id="petri_dish"/>放入左侧槽中. 3 秒后, 已分析的培养皿会移到右侧槽. 需先清空右侧槽, 下一个培养皿才能开始. 左侧槽只接受装有未分析菌落的培养皿, 因此管道永远不会被空的或已完成的培养皿堵塞.

各台机器也能处理未分析的菌落. 分析只是让你读取数值, 但你需要这些数值来选择要突变, 培养或燃烧哪个菌落. 从[诱变机](mutator.md)出来的菌落会再次变为未分析状态.

***

## <Color id="gold">搭建</Color>

分析机有两格方块高, 因此放置时其上方需要有一格空位. 右键点击任意一半即可打开.

它需要至少 5 AP 的光束从其底面下方进入. 功率是阈值而非消耗: 低于 5 AP 时它会暂停, 达到 5 AP 时以正常速度运行, 更强的光束会使其运行更快(见下文).

时间(60 tick)和功率(5 AP)均可配置.

漏斗和管道可以将培养皿送入下方方块, 并抽出已分析的培养皿, 默认可通过任意一面. [侧面配置](nautec:getting_started/utilities.md)可更改每一面允许的操作.

***

## <Color id="gold">读取已分析的培养皿</Color>

提示框会显示规模, 活力, 以及(对于能产出东西的菌株)菌株产量. 按住 Shift 可查看该菌株产出的物品及其四项属性. 同时按住 Shift 和 Control 还可查看菌落下次突变时每项属性可移动到的范围. Shift 还会列出该菌株在反应机中吃什么, 在培养机中生长在什么上, 以及它可以突变成的菌株, 并附上各自的催化剂和几率. 显示为红色的属性表示已达到上限. [细菌属性](bacteria_stats.md)解释了每一项.

***

## <Color id="gold">配方</Color>

<Recipe id="nautec:bacterial_analyzer"/>

***

## <Color id="gold">高级细菌分析机</Color>

<Row>
  <ItemImage id="advanced_bacterial_analyzer" scale="2"/>
</Row>

一次分析九个培养皿. 它有九个输入槽和九个输出槽, 输入中的每个培养皿会同时进行各自 60 tick 的分析, 因此满载完成的速度与基础分析机处理单个培养皿一样快. 每个输入槽会随着其培养皿的进度从底部填充.

* 能量: 至少 40 AP, 纯度 2.1 或更高的光束, 从除正面以外的任意一面输入. 低于其中任一项时, 它会暂停并保留进度. [海棱水晶](nautec:getting_started/laser_power.md)光束(3.0)或满纯度的<ItemLink id="bacterial_fuel_cell"/>(2.5)可满足纯度要求.
* 只接受装有未分析菌落的培养皿, 因此为其供料的管道永远不会被已完成或空的培养皿堵塞.
* 九个输出槽全部装满时, 已完成的培养皿会在其输入槽中等待, 直到有空位.

将鼠标悬停在箭头上可查看它在等待什么, 或通过<ItemLink id="prism_monocle"/>观察它. 漏斗和管道默认可通过任意一面为其供料并将其清空([侧面配置](nautec:getting_started/utilities.md)). 其时间, 功率和纯度在 `config/nautec-common.toml` 中.

<Recipe id="nautec:advanced_bacterial_analyzer"/>

***

## <Color id="gold">更强的光束</Color>

两种分析机在强于其需求的光束下都运行得更快: 速度为 (光束 ÷ 其需求量) 的平方根. 细菌分析机需要 5 AP, 因此 20 AP 的分析速度是两倍. 高级细菌分析机需要 40 AP, 纯度 2.1, 因此 160 AP 在该纯度下分析全部九个培养皿的速度是两倍. 纯度不会加速其中任何一台.

| 光束, 相对于其需求量的倍数 | 速度 |
|---|---|
| 1× | ×1 (正常) |
| 4× | ×2 |
| 9× | ×3 |
| 16× | ×4 |

细菌分析机每个培养皿 3 秒是在 5 AP 光束下的速度.

参见[更强的光束](nautec:getting_started/stronger_beams.md), 了解该规则及其适用的每台机器.
