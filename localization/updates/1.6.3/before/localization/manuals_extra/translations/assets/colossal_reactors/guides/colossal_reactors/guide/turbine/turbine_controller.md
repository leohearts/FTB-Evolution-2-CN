---
navigation:
  parent: turbine/turbine-index.md
  title: 涡轮机控制器
  icon: turbine_controller
  position: 20
item_ids:
  - colossal_reactors:turbine_controller
categories:
  - multiblock
---

# 涡轮机控制器

<BlockImage id="turbine_controller" scale="4" />

当涡轮机**建造正确**时, **右键点击**控制器以打开主界面.

第一次接触多方块结构? 请从[入门](colossal_reactors:turbine/getting_started.md)开始.

## 操作

- **启动和停止**涡轮机, 并在界面上查看 **RF 产出**, **蒸汽用量**与效率.

- 涡轮机运行时会不时重新检查; 如果某处损坏, 它会停止并说明原因(动作栏与 GUI 消息).

- 通常每个多方块结构只能有**一个**涡轮机控制器.

- 将其安装在外壳的**侧墙**上(世界中的北, 南, 东或西, 不是顶部或底部). 这与内部**转轴**的走向无关.

## 流体与能量

- **蒸汽**通过[涡轮机资源端口](turbine_resource_port.md)输入.

- **RF**通过[涡轮机能量端口](turbine_power_ports.md)输出.

- 用过的蒸汽通常会变成**水**(或你的整合包定义的其他流体), 见[蒸汽, RF 与线圈](turbine_generation_and_coils.md).

## 在不破坏方块的情况下停止

[涡轮机红石端口](turbine_redstone_port.md)可以通过外部红石关闭涡轮机, 同时保持结构完整, 其作用与[反应堆红石端口](../multiblock/redstone_port.md)相同.

控制器上显示的内容取决于你的**叶片布局**与**线圈方块**; 请在涡轮机内部调整它们, 而不只是在这个界面上操作.
