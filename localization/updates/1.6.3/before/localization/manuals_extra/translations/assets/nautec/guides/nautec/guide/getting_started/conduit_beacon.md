---
navigation:
  title: 潮涌信标
  icon: nautec:conduit_beacon
  position: 19
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:conduit_beacon
---

# <Color id="light_purple">潮涌信标</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="conduit_beacon" scale="2"/>
  一个由激光供能的潮涌核心, 同时还能阻止生物在你的基地周围生成.
</Column>

像建造原版潮涌核心那样建造它: 潮涌信标放在水中, 周围的 3 x 3 x 3 空间全部是水, 外面是由海晶石, 海晶石砖, 暗海晶石或海晶灯构成的框架. 启动至少需要 16 个框架方块, 完整框架为 42 个.

运行时它会做两件事:

* 为在水中或雨中的玩家提供潮涌能量, 效果与相同框架的潮涌核心一致. 16 个方块的框架范围为 32 格, 完整框架为 96 格.
* 在它水平方向 128 格内, 任何高度都不会自然生成敌对, 被动或环境生物. 刷怪笼, 刷怪蛋, 繁殖, 袭击以及鱼和鱿鱼等水生生物不受影响.

***

## <Color id="gold">能量</Color>

将激光束对准潮涌信标. 与它处在同一直线上的每个框架位置都算作框架的一部分, 因此请为光束留出一个缺口: 有光束穿过的框架槽位仍算作已填充, 所以完整框架仍能达到 96 格.

潮涌信标最多储存 5,000 AP. 输入的功率会存入其中, 潮涌信标以每 tick 50 AP 的速率消耗储存运行, 因此光束停止后它还会继续运行约 5 秒. 任何纯度都可以.

潮涌信标自身或任一框架方块收到红石信号时都会将其关闭. 由于潮涌信标总是被水包围, 请把拉杆或红石线放在框架方块上.

透过<ItemLink id="prism_monocle"/>查看它, 可看到其状态, 框架大小, 范围和储存的能量.

功率消耗, 储量和生成半径分别对应 `config/nautec-common.toml` 中的 `conduitBeaconPowerUsage`, `conduitBeaconBuffer` 和 `conduitBeaconSpawnRadius`.

<RecipeFor id="conduit_beacon"/>
