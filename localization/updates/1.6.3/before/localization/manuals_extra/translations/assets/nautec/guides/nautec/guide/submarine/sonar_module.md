---
navigation:
  title: 声呐模块
  icon: nautec:sonar_module
  position: 11
  parent: submarine/submarine-index.md
item_ids:
  - nautec:sonar_module
---

# <Color id="light_purple">声呐模块</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="sonar_module" scale="2"/>
  透过岩石探测矿石与敌对生物.
</Column>

声呐模块的一次扫描会透过实心岩石标记 48 格内的所有矿脉和 32 格内的所有敌对生物, 并给予乘员夜视效果.

***

## <Color id="gold">使用</Color>

| | 默认 |
|---|---|
| 每次扫描能量 | 30,000 |
| 矿石范围 | 48 格 |
| 敌对生物范围 | 32 格 |
| 冷却 | 45 秒 |

发射后, 一道环形波会从艇体向外扫过地形. 每个矿脉在环波到达时被勾勒出来, 颜色按矿石种类区分, 并在岩石后保持标记 45 秒, 结束时逐渐淡出. 任何被通用矿石标签视为矿石的对象都会显示, 因此其他模组的矿石也会出现.

扫描时 32 格内的敌对生物会被红色轮廓标记同样的 45 秒, 并随其移动, 同时还会发光 15 秒.

艇上所有人都会获得 45 秒夜视, 这在光线难以到达的深水中很重要.

两个范围都以艇体扫描时所处位置为起点, 因此移动后要再次扫描才能探测新的区域. 能量消耗, 敌对生物范围和冷却时间都可配置.

***

### <Color id="aqua">声呐模块配方</Color>

<Recipe id="nautec:sonar_module"/>
