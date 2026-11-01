---
title: 水泵
entryId: stellaris:machines
iconType: item
associatedBlocks: [stellaris:water_pump]
---

水泵从世界中抽取水, 并送入你的流体网络.

[item=stellaris:water_pump scale=5]

**使用方法:**
把水泵**直接放在水源方块上方**, 并为其供电.其他方式都不行: 水泵旁边或低一格的含水方块都会被忽略.

每个周期它会吞掉下方的水源方块并储存 1 000 mB 的水, 然后把这些水从**顶部**面推出.在上方接一根 [ref=stellaris:machines/pipes]管道[ref], 把水送到 [ref=stellaris:machines/electrolyzer]电解器[ref] 或 [ref=stellaris:machines/fluid_tank]流体储罐[ref].

由于水源方块会被消耗, 请把水泵建在无限水源上方, 让水能流回来, 这样水泵就永远不会抽干.



**统计数据:**
- 功耗: 每抽取 1 000 mB 消耗 1 500 FE
- 储罐容量: 1 000 mB
- 内部缓存: 1 500 FE
