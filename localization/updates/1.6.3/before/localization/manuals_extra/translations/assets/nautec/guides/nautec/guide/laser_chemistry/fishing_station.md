---
navigation:
  title: 钓鱼站
  icon: nautec:fishing_station
  position: 11
  parent: laser_chemistry/laser_chemistry-index.md
item_ids:
  - nautec:fishing_station
---

# <Color id="light_purple">钓鱼站</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="fishing_station" scale="2"/>
  自动钓鱼并储存渔获.
</Column>

## <Color id="gold">放置</Color>

将其放置在开阔水域上方. 其下方 5x5 区域内的每个方块, 深两格, 都必须是普通水. 该区域内任何位置的海带, 海草, 含水方块或盐水都会使其停止, 因此请清理该区域或另选干净的位置.

它每五秒检查一次水. 工作时渔网会转动.

***

## <Color id="gold">能量</Color>

将光束对准其顶部或底部. 任意功率都能驱动它(每 tick 1 AP, 可配置), 且纯度无关.

***

## <Color id="gold">产出</Color>

它每两秒(可配置)掷一次普通钓鱼战利品, 并将渔获储存在 15 个槽位中. 右键点击可打开并取出渔获, 或用漏斗或管道从任意一面抽出. 槽位满后, 多出的渔获会以物品形式从钓鱼站掉出.

***

### <Color id="aqua">钓鱼站配方</Color>

<RecipeFor id="fishing_station"/>
