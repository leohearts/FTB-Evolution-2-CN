---
navigation:
  title: 深海生物强化
  icon: nautec:abyssal_organ
  position: 5
  parent: laser_augmentation/laser_augmentation-index.md
item_ids:
  - nautec:abyssal_organ
  - nautec:luminous_membrane
  - nautec:chitin_plate
---

# <Color id="light_purple">深海生物强化</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="abyssal_organ" scale="2"/>
  有三种强化来自 海蓝科技 海洋生物群系中的生物.
</Column>

这些生物总会掉落其部件, 抢夺附魔还可以额外增加一个. [深海生命](nautec:getting_started/deep_life.md)介绍了每种生物的生成位置. 这三种部件也都有可能从幸运钓鱼区获得(见[钓鱼](nautec:getting_started/fishing.md)).

***

<Row>
  <ItemImage id="abyssal_organ"/>
  ### <Color id="aqua">深渊之眼</Color>
</Row>

部件: 深渊器官, 每只深渊巨口掉落一个. 深渊巨口在 Y 40 以下的深渊海沟中捕猎.

槽位: 眼睛. 当你在 Y 45 或更低位置时给予你夜视效果(可配置, `abyssalEyesDepth`). 高于该高度时没有任何效果, 并且上升越过该高度后效果会在约十秒内消失.

它与 <ItemLink id="guardian_eye"/> 共用眼睛槽位.

***

<Row>
  <ItemImage id="luminous_membrane"/>
  ### <Color id="aqua">发光皮肤</Color>
</Row>

部件: 发光膜, 荧光海林中的每只灯笼水母掉落一到两个.

槽位: 身体. 当你在水中时, 你周围 12 格内的所有生物都会发光, 并且轮廓可以透过方块显示(可配置, `photophoreSkinRadius`). 离开水中则没有任何效果.

它占用身体槽位, 与飞行和海豚鳍占用同一个槽位.

***

<Row>
  <ItemImage id="chitin_plate"/>
  ### <Color id="aqua">热泉甲壳</Color>
</Row>

部件: 四个甲壳板, 四个扩展单元中各放一个. 海底热泉中的每只热泉爬行者掉落一到三个. 每个放有甲壳板的扩展单元都需要自己的爪式机械臂和自己的 25 AP 激光束(见[强化站](augmentation_station.md)).

槽位: 头部或身体. 增加 4 点护甲和 50% 击退抗性, 并且火焰灼烧你的时间减半. 把它放在头部槽位可以为其他强化保留身体槽位. 在另一个槽位再放一个甲壳不会提供任何额外效果.
