---
navigation:
  title: 水下基地
  icon: nautec:pressure_hatch
  position: 18
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:pressure_hatch
  - nautec:oxygen_diffuser
---

# <Color id="light_purple">水下基地</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="pressure_hatch" scale="2"/>
  用于在海底建造干燥永久基地的方块.
</Column>

先用[气泡锚](bubble_anchor.md)清出空间, 用墙围住, 并把锚设置为结束时留下空气. 之后这些方块会让房间保持干燥.

***

## <Color id="gold">压力舱门</Color>

一扇带舷窗的钢门, 两格高. 可以用手或红石开关.

* 无论开启还是关闭, 海水都不会穿过它, 因此你可以从打开的舱门游进去, 而它后面的房间保持干燥.
* 每次关闭时, 它都会抽出两侧的水, 只要那些水是一小团: 你带进来的水, 被淹没的门口, 一处渗漏. 一次最多可清除 64 格相连的水.
* 属于海洋一部分的水, 或大于 64 格的淹没房间, 不会被处理, 因此关闭舱门绝不会排干外面的海洋.

在水中放置舱门会清除它所占据的两个方块, 因此可以直接把它装进被淹没的门口.

<RecipeFor id="pressure_hatch"/>

***

## <Color id="gold">氧气扩散器</Color>

<ItemImage id="oxygen_diffuser" scale="2"/>

为 12 格内的每位玩家提供水下呼吸并保持氧气充足, 因此你可以在基地周围的开放水域中不戴头盔工作.

* 它需要至少 10 AP 的激光束射入任意一面. 纯度无关紧要, 因此早期最弱的光束就能驱动它.
* 光束持续期间, 它每秒刷新该效果. 走出范围后, 效果会在几秒后结束.
* 它可以放在水下. 运行时顶部会冒出气泡.
* 如果光束短暂中断, 它会继续运行两秒然后停止.

范围和功率在 `config/nautec-common.toml` 中.

<RecipeFor id="oxygen_diffuser"/>
