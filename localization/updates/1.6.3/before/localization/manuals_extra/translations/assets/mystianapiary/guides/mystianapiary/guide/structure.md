---
navigation:
  title: 蜂房结构
  parent: index.md
  icon: minecraft:honeycomb_block
  position: 1
---

# 蜂房结构

Mystian Apiary 是一个 **3x3x3 多方块结构**, 让你的资源蜜蜂原地工作, 因此蜜蜂永远不会离开它.

它的核心是一个**蜜脾块**, 外面包裹着由**原木**构成的立方体, 四个箱子嵌在它的侧面上.

## 搭建

从中间向外:

- **中心**: 一个蜜脾块
- 它**北, 南, 东, 西**四个方向: 分别放置[蜂房蜜蜂箱](modules.md#bee-box), [蜂房花箱](modules.md#flower-box), [蜂房存储](modules.md#storage)和[蜂房控制器](modules.md#controller)各一个, 排列顺序任意
- 立方体中的**其他所有位置**: 任意原木, 普通或去皮均可

<GameScene zoom="6">
  <Block x="0" y="0" z="0" id="minecraft:oak_log" />
  <Block x="1" y="0" z="0" id="minecraft:oak_log" />
  <Block x="2" y="0" z="0" id="minecraft:oak_log" />
  <Block x="0" y="0" z="1" id="minecraft:oak_log" />
  <Block x="1" y="0" z="1" id="minecraft:oak_log" />
  <Block x="2" y="0" z="1" id="minecraft:oak_log" />
  <Block x="0" y="0" z="2" id="minecraft:oak_log" />
  <Block x="1" y="0" z="2" id="minecraft:oak_log" />
  <Block x="2" y="0" z="2" id="minecraft:oak_log" />
  <Block x="0" y="1" z="0" id="minecraft:oak_log" />
  <Block x="1" y="1" z="0" id="mystianapiary:input_block" p:facing="west" />
  <Block x="2" y="1" z="0" id="minecraft:oak_log" />
  <Block x="0" y="1" z="1" id="mystianapiary:flower_block" p:facing="south" />
  <Block x="1" y="1" z="1" id="minecraft:honeycomb_block" />
  <Block x="2" y="1" z="1" id="mystianapiary:upgrade_block" />
  <Block x="0" y="1" z="2" id="minecraft:oak_log" />
  <Block x="1" y="1" z="2" id="mystianapiary:output_block" p:facing="east" />
  <Block x="2" y="1" z="2" id="minecraft:oak_log" />
  <Block x="0" y="2" z="0" id="minecraft:oak_log" />
  <Block x="1" y="2" z="0" id="minecraft:oak_log" />
  <Block x="2" y="2" z="0" id="minecraft:oak_log" />
  <Block x="0" y="2" z="1" id="minecraft:oak_log" />
  <Block x="1" y="2" z="1" id="minecraft:oak_log" />
  <Block x="2" y="2" z="1" id="minecraft:oak_log" />
  <Block x="0" y="2" z="2" id="minecraft:oak_log" />
  <Block x="1" y="2" z="2" id="minecraft:oak_log" />
  <Block x="2" y="2" z="2" id="minecraft:oak_log" />
</GameScene>

## 可选: 第二个存储箱

需要更多空间? **蜜脾块正上方**的那根原木 (顶部中央) 可以替换为任意等级的**第二个存储箱**. 产物会先填满侧面的主存储箱, 只有该箱满了才会溢出到第二个箱子, 不过第二个箱子中未满的一组总是会被优先补满. 流体也以同样的方式溢出.

在那里放原木也完全可以, 第二个箱子完全是可选的 (服主可以通过 `allowSecondOutput` 配置禁用它).

<GameScene zoom="6">
  <Block x="0" y="0" z="0" id="minecraft:oak_log" />
  <Block x="1" y="0" z="0" id="minecraft:oak_log" />
  <Block x="2" y="0" z="0" id="minecraft:oak_log" />
  <Block x="0" y="0" z="1" id="minecraft:oak_log" />
  <Block x="1" y="0" z="1" id="minecraft:oak_log" />
  <Block x="2" y="0" z="1" id="minecraft:oak_log" />
  <Block x="0" y="0" z="2" id="minecraft:oak_log" />
  <Block x="1" y="0" z="2" id="minecraft:oak_log" />
  <Block x="2" y="0" z="2" id="minecraft:oak_log" />
  <Block x="0" y="1" z="0" id="minecraft:oak_log" />
  <Block x="1" y="1" z="0" id="mystianapiary:input_block" p:facing="west" />
  <Block x="2" y="1" z="0" id="minecraft:oak_log" />
  <Block x="0" y="1" z="1" id="mystianapiary:flower_block" p:facing="south" />
  <Block x="1" y="1" z="1" id="minecraft:honeycomb_block" />
  <Block x="2" y="1" z="1" id="mystianapiary:upgrade_block" />
  <Block x="0" y="1" z="2" id="minecraft:oak_log" />
  <Block x="1" y="1" z="2" id="mystianapiary:output_block" p:facing="east" />
  <Block x="2" y="1" z="2" id="minecraft:oak_log" />
  <Block x="0" y="2" z="0" id="minecraft:oak_log" />
  <Block x="1" y="2" z="0" id="minecraft:oak_log" />
  <Block x="2" y="2" z="0" id="minecraft:oak_log" />
  <Block x="0" y="2" z="1" id="minecraft:oak_log" />
  <Block x="1" y="2" z="1" id="mystianapiary:output_block" p:facing="north" />
  <Block x="2" y="2" z="1" id="minecraft:oak_log" />
  <Block x="0" y="2" z="2" id="minecraft:oak_log" />
  <Block x="1" y="2" z="2" id="minecraft:oak_log" />
  <Block x="2" y="2" z="2" id="minecraft:oak_log" />
</GameScene>
