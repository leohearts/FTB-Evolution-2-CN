---
navigation:
  title: 太阳能模块
  icon: nautec:solar_module
  position: 7
  parent: submarine/submarine-index.md
item_ids:
  - nautec:solar_module
---

# <Color id="light_purple">太阳能模块</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="solar_module" scale="2"/>
  依靠日光被动充能.
</Column>

当太阳高照且艇体能看到天空时, 太阳能模块每 5 秒为艇体增加 2,000 能量(电池的 0.2%, 约每刻 20).

***

## <Color id="gold">充能方式</Color>

它属于被动模块, 放在任意槽位都生效. 它能透过水看到天空, 因此艇体可以保持在水下, 但艇体与天空之间有任何固体方块都会使其停止工作. 它只在白天工作, 在下界和末地等没有昼夜周期的维度中无效.

无人乘坐时它也会继续充能. 停在开阔水域的艇体在阳光下约 42 分钟可从空充满. [海洋侦察艇船坞](submarine_dock.md)的速度是它的两倍.

一个模块就够, 第二个不会提供额外效果. 该速率可配置(`submarineSolarPercentPer5s`).

***

### <Color id="aqua">太阳能模块配方</Color>

<Recipe id="nautec:solar_module"/>
