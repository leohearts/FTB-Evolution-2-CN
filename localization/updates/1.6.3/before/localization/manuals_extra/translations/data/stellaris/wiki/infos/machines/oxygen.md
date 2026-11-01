---
title: 氧气系统
entryId: stellaris:machines
iconType: item
associatedBlocks: [stellaris:oxygen_propagator,stellaris:oxygen_distributor]
overrideTitle: true
---

氧气系统是宇宙中最重要的系统.在地球之外, 没有氧气的区域每秒会对任何呼吸的生物造成 0.5 点伤害.

[image=stellaris:textures/wiki/rendered_blocks/oxygen_distributor width=96 height=96]

**氧气分配器**

氧气分配器为密闭房间充满可呼吸的空气.为它提供能量和氧气, 氧气可以通过来自 [ref=stellaris:machines/electrolyzer]电解器[ref] 的 [ref=stellaris:machines/pipes]管道[ref] 输入, 也可以直接用输入槽中的 [ref=stellaris:items/fluid_cell]流体胶囊[ref] 提供.

房间由从分配器扩散到每一个可通行方块的空气填充, 并且必须遵守三条规则:
- 房间必须**与天空完全隔绝**.如果空气到达任何一处上方毫无遮挡的位置, 整个房间就会失去氧气.玻璃屋顶仍算作密封, 只有真正的开口才会泄漏.
- 房间必须位于 **3 x 3 区块**以内, 范围为世界的整个高度.该区域是围绕房间本身计算的, 而不是围绕机器, 所以分配器可以放在区域内的任何位置, 放在角落也可以.无法容纳的房间会完全失去氧气.
- 一个房间最多可容纳 50 000 格空气.

氧气只消耗在呼吸上: 每个更新周期, 房间内每个活着的生物消耗 1 mB.空房间除了能量之外不产生任何消耗.穿着充满氧气头盔的完整 [ref=stellaris:items/space_suit]航天服[ref] 的玩家会改为从航天服呼吸, 不消耗分配器任何氧气.



**统计数据:**
- 能量消耗: 每个更新周期 15 FE, 默认每秒一次更新
- 氧气消耗: 每个更新周期每个呼吸的生物 1 mB
- 储罐容量: 10 000 mB
- 内部缓存: 192 000 FE

[image=stellaris:textures/wiki/rendered_blocks/oxygen_propagator width=96 height=96]

**氧气扩散器**

氧气扩散器可扩展分配器的覆盖范围.它需要能量, 但本身不需要氧气.

通电时, 它会把自己所在的 3 x 3 区块加入分配器允许填充的区域, 前提是它位于已经允许的区域内.这些区块内的空气不计入分配器自身的 3 x 3 限额, 因此串联多个扩散器可以让空气沿长走廊或穿过大型基地输送, 而没有总量上限.未通电的扩散器不会提供任何扩展.



*趣闻*: 火没有氧气就无法燃烧.火把没有问题, 但在没有氧气的房间外, 火焰会立刻熄灭, 普通作物也拒绝生长, 甚至无法种植.使用 [ref=stellaris:machines/space_farm]太空农场[ref] 就能在没有空气的地方耕作.

[item=stellaris:oxygen_distributor onlyIcon]
