---
navigation:
  title: 生物强化
  icon: nautec:dolphin_fin
  position: 3
  parent: laser_augmentation/laser_augmentation-index.md
item_ids:
  - nautec:guardian_eye
  - nautec:dolphin_fin
  - nautec:drowned_lungs
  - nautec:eldritch_heart
---

# <Color id="light_purple">生物强化</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="dolphin_fin" scale="2"/>
  有四种强化来自原版海洋生物掉落的器官.
</Column>

每种器官在掉落时就可以拿到[强化站](augmentation_station.md)安装, 无需合成.

***

<Row>
  <ItemImage id="guardian_eye"/>
  ### <Color id="aqua">守卫者之眼</Color>
</Row>

槽位: 眼睛. 由守卫者掉落, 约每击杀四十只掉落一个.

按住 L 可沿你的视线向第一个生物发射守卫者光束, 最远 15 格. 光束会被第一个固体方块挡住, 因此你需要与目标之间保持通畅的视线. 水不会阻挡它. 每次命中造成 3 点魔法伤害(可配置, `guardianAugmentDamage`), 并且只要你按住按键就会持续发射, 没有冷却, 也不消耗能量.

它与深渊之眼共用眼睛槽位.

***

<Row>
  <ItemImage id="dolphin_fin"/>
  ### <Color id="aqua">海豚鳍</Color>
</Row>

槽位: 身体. 由海豚掉落, 约每击杀五只掉落一个.

当你的头部浸入水中时, 会获得海豚的恩惠 II, 因此游动速度大幅提升. 它占用身体槽位, 与飞行和发光皮肤占用同一个槽位.

***

<Row>
  <ItemImage id="drowned_lungs"/>
  ### <Color id="aqua">溺尸之肺</Color>
</Row>

槽位: 肺部. 由溺尸掉落, 约每击杀二十只掉落一个.

在水下时会让你的氧气条保持满值, 因此你永远不会溺水. 它是肺部槽位唯一的强化, 因此从不与其他强化竞争.

***

<Row>
  <ItemImage id="eldritch_heart"/>
  ### <Color id="aqua">邪能之心</Color>
</Row>

槽位: 心脏. 由远古守卫者掉落: 每只约有五分之三的概率掉落至少一个.

当你在水中时, 每秒为你恢复半颗心.

合成强化站也需要一个邪能之心, 所以第一个请留作此用. 它与[合成强化](crafted_augments.md)中的辅助心室共用心脏槽位, 后者改为使你的最大生命值翻倍.
